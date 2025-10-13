from django.utils import timezone
from datetime import datetime, timedelta
from event.models import EventForm, Event, EventFormField

def seed_events():
    # Primeiro cria o formulário do evento
    event_form = EventForm.objects.create(
        name='Formulário de Inscrição - Evento Ciclístico',
        description='Formulário para inscrição no evento de ciclismo'
    )
    
    # Campos do formulário
    form_fields = [
        {
            'name': 'emergency_contact',
            'label': 'Contato de Emergência',
            'type': 'text',
            'required': 1,
            'order': 1,
            'form': event_form
        },
        {
            'name': 'medical_conditions',
            'label': 'Condições Médicas',
            'type': 'textarea',
            'required': 0,
            'order': 2,
            'form': event_form
        },
        {
            'name': 'bike_type',
            'label': 'Tipo de Bicicleta',
            'type': 'select',
            'required': 1,
            'options': 'Mountain Bike;Speed;Urbana;Outro',
            'order': 3,
            'form': event_form
        }
    ]
    
    for field_data in form_fields:
        EventFormField.objects.create(**field_data)
    
    # Cria o evento
    event = Event.objects.create(
        name='Pedal da Primavera 2024',
        description='Um evento incrível de ciclismo pela cidade',
        date=datetime.now().date() + timedelta(days=30),
        secondary_date=datetime.now().date() + timedelta(days=31),
        latitude=-23.550520,
        longitude=-46.633308,
        location='Parque Ibirapuera - São Paulo',
        status='active',
        banner_image='events/pedal_primavera_banner.jpg',
        zoom=13,
        pdf_file='events/regulamento_pedal_primavera.pdf',
        created_at=timezone.now(),
        updated_at=timezone.now(),
        form=event_form
    )
    
    print("Events and forms seeded successfully!")