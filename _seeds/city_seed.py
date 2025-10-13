from django.utils import timezone
from cities.models import City

def seed_cities():
    cities = [
        {
            'name': 'São Paulo',
            'banner_image': 'cities/sao_paulo_banner.jpg',
            'latitude': -23.550520,
            'longitude': -46.633308,
            'active': 1,
            'visible': 1,
            'zoom': 12,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        },
        {
            'name': 'Rio de Janeiro',
            'banner_image': 'cities/rio_banner.jpg',
            'latitude': -22.906847,
            'longitude': -43.172896,
            'active': 1,
            'visible': 1,
            'zoom': 12,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        },
        {
            'name': 'Belo Horizonte',
            'banner_image': 'cities/bh_banner.jpg',
            'latitude': -19.916681,
            'longitude': -43.934493,
            'active': 1,
            'visible': 1,
            'zoom': 12,
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        }
    ]
    
    for city_data in cities:
        City.objects.create(**city_data)
    
    print("Cities seeded successfully!")