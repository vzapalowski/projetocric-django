from django.utils import timezone
from core.models import Anchorpoint, AnchorpointCategory

def seed_anchorpoints():
    # Primeiro obtenha as categorias
    park_category = AnchorpointCategory.objects.get(icon_name='park')
    square_category = AnchorpointCategory.objects.get(icon_name='square')
    viewpoint_category = AnchorpointCategory.objects.get(icon_name='viewpoint')
    
    anchorpoints = [
        {
            'name': 'Parque Ibirapuera',
            'latitude': -23.587674,
            'longitude': -46.655512,
            'business_hours': '05:00-00:00',
            'phone': '(11) 5574-5045',
            'image': 'anchorpoints/ibirapuera.jpg',
            'address': 'Av. Pedro Álvares Cabral - Vila Mariana, São Paulo - SP',
            'is_event_anchorpoint': 1,
            'active': 1,
            'anchorpoint_category': park_category
        },
        {
            'name': 'Praça da Sé',
            'latitude': -23.550348,
            'longitude': -46.633869,
            'business_hours': '24 horas',
            'phone': '',
            'image': 'anchorpoints/praca_se.jpg',
            'address': 'Praça da Sé - Sé, São Paulo - SP',
            'is_event_anchorpoint': 1,
            'active': 1,
            'anchorpoint_category': square_category
        },
        {
            'name': 'Mirante do Parque do Povo',
            'latitude': -23.599678,
            'longitude': -46.687119,
            'business_hours': '06:00-20:00',
            'phone': '',
            'image': 'anchorpoints/mirante_povo.jpg',
            'address': 'Av. Henrique Chamma, 420 - Itaim Bibi, São Paulo - SP',
            'is_event_anchorpoint': 0,
            'active': 1,
            'anchorpoint_category': viewpoint_category
        }
    ]
    
    for anchorpoint_data in anchorpoints:
        Anchorpoint.objects.create(**anchorpoint_data)
    
    print("Anchorpoints seeded successfully!")