from django.utils import timezone
from event.models import Warning

def seed_warnings():
    warnings = [
        {
            'title': 'Chuva Prevista',
            'content': 'Há previsão de chuva para o dia do evento. Traga capa de chuva e tenha cuidado redobrado.',
            'created_at': timezone.now()
        },
        {
            'title': 'Obras na Via',
            'content': 'Há obras na Avenida Paulista. O trajeto foi ajustado para evitar a região.',
            'created_at': timezone.now()
        },
        {
            'title': 'Equipamento Obrigatório',
            'content': 'Lembre-se que capacete é item obrigatório para participação no evento.',
            'created_at': timezone.now()
        }
    ]
    
    for warning_data in warnings:
        Warning.objects.create(**warning_data)
    
    print("Warnings seeded successfully!")