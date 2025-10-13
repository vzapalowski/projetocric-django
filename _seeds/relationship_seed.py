from django.utils import timezone
from your_app.models import (
    CityAnchorpoint, CityImage, CityRoute, EventAnchorpoint, 
    EventEnrollment, EventImage, EventParticipants, EventRoute,
    EventWarning, HomeAnchorpointsmanager, HomeCitymanager, HomeHome
)
from your_app.models import City, Anchorpoint, Route, Event, AuthUser, Warning

def seed_relationships():
    # Obter instâncias existentes
    sao_paulo = City.objects.get(name='São Paulo')
    rio = City.objects.get(name='Rio de Janeiro')
    
    parque_ibirapuera = Anchorpoint.objects.get(name='Parque Ibirapuera')
    praca_se = Anchorpoint.objects.get(name='Praça da Sé')
    
    rota_centro = Route.objects.get(name='Rota Centro Histórico')
    rota_ibirapuera = Route.objects.get(name='Rota Parque Ibirapuera')
    
    evento_principal = Event.objects.first()
    
    users = AuthUser.objects.all()
    warnings = Warning.objects.all()

    # CityAnchorpoint
    CityAnchorpoint.objects.create(city=sao_paulo, anchorpoint=parque_ibirapuera)
    CityAnchorpoint.objects.create(city=sao_paulo, anchorpoint=praca_se)

    # CityImage
    CityImage.objects.create(
        image_path='cities/sao_paulo_1.jpg',
        title='Vista Aérea de São Paulo',
        subtitle='A maior cidade do Brasil',
        city=sao_paulo
    )
    CityImage.objects.create(
        image_path='cities/sao_paulo_2.jpg',
        title='Centro Histórico',
        subtitle='Patrimônio cultural',
        city=sao_paulo
    )

    # CityRoute
    CityRoute.objects.create(city=sao_paulo, route=rota_centro)
    CityRoute.objects.create(city=sao_paulo, route=rota_ibirapuera)

    # EventAnchorpoint
    EventAnchorpoint.objects.create(event=evento_principal, anchorpoint=parque_ibirapuera)

    # EventEnrollment
    for user in users:
        EventEnrollment.objects.create(
            created_at=timezone.now(),
            updated_at=timezone.now(),
            event=evento_principal,
            route=rota_centro,
            user=user
        )

    # EventImage
    EventImage.objects.create(
        image_path='events/pedal_primavera_1.jpg',
        event=evento_principal
    )
    EventImage.objects.create(
        image_path='events/pedal_primavera_2.jpg',
        event=evento_principal
    )

    # EventParticipants
    for user in users:
        EventParticipants.objects.create(event=evento_principal, user=user)

    # EventRoute
    EventRoute.objects.create(
        name='Rota Principal - Pedal da Primavera',
        time='07:00',
        departure_location='Portão 3 do Parque Ibirapuera',
        concentration='06:30',
        active=1,
        event=evento_principal,
        route=rota_ibirapuera
    )

    # EventWarning
    for warning in warnings[:2]:  # Primeiros 2 warnings
        EventWarning.objects.create(event=evento_principal, warning=warning)

    # Home managers
    HomeAnchorpointsmanager.objects.create(anchor_point=parque_ibirapuera)
    HomeCitymanager.objects.create(city=sao_paulo)

    # HomeHome (configuração principal)
    HomeHome.objects.create(
        name='Configuração Principal',
        lat='-23.550520',
        lng='-46.633308',
        zoom=10
    )

    print("Relationship seeds completed successfully!")