import pytest
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from core.models import Route
from event.models import Event, Enrollment, EventRoute
from event.models.event_form import EventForm
from event.models.event_form_field import EventFormField
from event.models.event_form_response import EventFormResponse


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="tester", password="secret")


@pytest.fixture
def event_form(db):
    form = EventForm.objects.create(name="Ficha de Inscrição")
    field = EventFormField.objects.create(
        form=form,
        name="full_name",
        label="Nome completo",
        type="text",
        required=True,
        order=1,
    )
    return form, field


@pytest.fixture
def base_event(db, event_form):
    form, _ = event_form
    return Event.objects.create(name="Passeio", form=form)


@pytest.fixture
def route(db):
    return Route.objects.create(external_strava_id="r1", name="Rota 1")


@pytest.fixture
def event_route(db, base_event, route):
    return EventRoute.objects.create(
        event=base_event,
        route=route,
        name="Trajeto A",
        time="08:00",
        departure_location="Praça Central",
        active=True,
    )


@pytest.mark.django_db
def test_enrollment_success(client, user, base_event, event_route, event_form):
    form, field = event_form
    client.force_login(user)

    url = reverse("events:enrollment", args=[base_event.id])
    response = client.post(
        url,
        {
            "route_path": event_route.id,
            f"field_{field.id}": "João Teste",
        },
    )

    assert response.status_code == 302
    assert response.url.startswith(reverse("events:enrollment_success"))

    enrollment = Enrollment.objects.get()
    assert enrollment.user == user
    assert enrollment.route == event_route

    event = enrollment.event
    event.refresh_from_db()
    assert event.participants.filter(id=user.id).exists()

    form_response = EventFormResponse.objects.get(enrollment=enrollment, field=field)
    assert form_response.value == "João Teste"


@pytest.mark.django_db
def test_enrollment_missing_required_field(client, user, base_event, event_route, event_form):
    _, field = event_form
    client.force_login(user)

    url = reverse("events:enrollment", args=[base_event.id])
    response = client.post(url, {"route_path": event_route.id}, follow=True)

    assert response.status_code == 200
    assert Enrollment.objects.count() == 0

    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert any("Por favor, preencha os campos obrigatórios" in msg for msg in messages)
    assert any(field.label in msg for msg in messages)


@pytest.mark.django_db
def test_enrollment_with_inactive_route(client, user, base_event, event_route, event_form):
    form, field = event_form
    client.force_login(user)

    event_route.active = False
    event_route.save()

    url = reverse("events:enrollment", args=[base_event.id])
    response = client.post(
        url,
        {
            "route_path": event_route.id,
            f"field_{field.id}": "João Teste",
        },
        follow=True,
    )

    assert response.status_code == 200
    assert Enrollment.objects.count() == 0

    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert any("Rota selecionada não está disponível." in msg for msg in messages)


@pytest.mark.django_db
def test_enrollment_without_form(client, user):
    event = Event.objects.create(name="Passeio sem formulário")
    client.force_login(user)

    url = reverse("events:enrollment", args=[event.id])
    response = client.post(url, follow=True)

    assert response.status_code == 200
    assert Enrollment.objects.count() == 0

    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert any("não possui formulário de inscrição" in msg for msg in messages)