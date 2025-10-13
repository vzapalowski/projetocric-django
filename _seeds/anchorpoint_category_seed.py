from django.utils import timezone
from core.models import AnchorpointCategory

def seed_anchorpoint_categories():
    categories = [
        {
            'name': 'Parques',
            'icon_name': 'park',
            'is_active': 1,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        },
        {
            'name': 'Praças',
            'icon_name': 'square',
            'is_active': 1,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        },
        {
            'name': 'Mirantes',
            'icon_name': 'viewpoint',
            'is_active': 1,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        },
        {
            'name': 'Centros Culturais',
            'icon_name': 'cultural_center',
            'is_active': 1,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        },
        {
            'name': 'Estações',
            'icon_name': 'station',
            'is_active': 1,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        }
    ]
    
    for category_data in categories:
        AnchorpointCategory.objects.create(**category_data)
    
    print("Anchorpoint categories seeded successfully!")