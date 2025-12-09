import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db import transaction

from core.models import Route
from event.models import Event, Enrollment, EventRoute
from event.models.event_form import EventForm
from event.models.event_form_field import EventFormField
from event.models.event_form_response import EventFormResponse
from event.models.warning import Warning


@pytest.fixture
def user(db):
    return User.objects.create_user(username="model-tester", password="secret")


@pytest.fixture
def event(db):
    return Event.objects.create(name="Passeio da Serra")


@pytest.fixture
def route(db):
    return Route.objects.create(external_strava_id="strava-001", name="Rota Azul")


@pytest.fixture
def event_route(db, event, route):
    return EventRoute.objects.create(
        event=event,
        route=route,
        name="Trajeto Principal",
        time="08:00",
        departure_location="Praça Central",
        active=True,
    )


@pytest.fixture
def event_form(db):
    return EventForm.objects.create(name="Ficha")


@pytest.fixture
def event_form_field(db, event_form):
    return EventFormField.objects.create(
        form=event_form,
        name="full_name",
        label="Nome Completo",
        type="text",
        required=True,
        order=1,
    )


@pytest.fixture
def enrollment(db, user, event, event_route):
    return Enrollment.objects.create(user=user, event=event, route=event_route)


@pytest.mark.django_db
def test_event_str_returns_name(event):
    assert str(event) == "Passeio da Serra"


@pytest.mark.django_db
def test_event_route_str_and_unique_constraint(event, route):
    EventRoute.objects.create(
        event=event,
        route=route,
        name="Trajeto A",
        time="08:00",
        departure_location="Praça Central",
        active=True,
    )

    # Wrap in atomic to avoid broken transaction on MySQL after IntegrityError
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            EventRoute.objects.create(
                event=event,
                route=route,
                name="Trajeto A duplicado",
                time="09:00",
                departure_location="Outro local",
                active=True,
            )

    assert str(EventRoute.objects.get(event=event, route=route)) == "Trajeto A"


@pytest.mark.django_db
def test_enrollment_unique_per_event_and_user(user, event, event_route):
    Enrollment.objects.create(user=user, event=event, route=event_route)

    with pytest.raises(IntegrityError):
        Enrollment.objects.create(user=user, event=event, route=event_route)


@pytest.mark.django_db
def test_event_form_response_str(enrollment, event_form_field):
    response = EventFormResponse.objects.create(
        enrollment=enrollment,
        field=event_form_field,
        value="João",
    )

    string_repr = str(response)
    assert enrollment.user.username in string_repr
    assert enrollment.event.name in string_repr
    assert event_form_field.name in string_repr


@pytest.mark.django_db
def test_warning_str(event):
    warning = Warning.objects.create(title="Aviso", content="Use capacete", event=event)
    assert str(warning) == "Aviso"