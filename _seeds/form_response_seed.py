from django.utils import timezone
from event.models import EventFormResponse, EventEnrollment, EventFormField

def seed_form_responses():
    # Obter todas as inscrições e campos do formulário
    enrollments = EventEnrollment.objects.all()
    form_fields = EventFormField.objects.all()
    
    for enrollment in enrollments:
        for field in form_fields:
            if field.name == 'emergency_contact':
                value = '(11) 99999-9999'
            elif field.name == 'medical_conditions':
                value = 'Nenhuma'
            elif field.name == 'bike_type':
                value = 'Mountain Bike'
            else:
                value = 'Resposta padrão'
            
            EventFormResponse.objects.create(
                value=value,
                enrollment=enrollment,
                field=field
            )
    
    print("Form responses seeded successfully!")