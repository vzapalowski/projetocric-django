from core.models import Route

def seed_routes():
    routes = [
        {
            'external_strava_id': 'strava_12345',
            'name': 'Rota Centro Histórico',
            'polyline': 'mock_polyline_data_1',
            'color': '#FF0000',
            'distance': '15.5',
            'active': 1
        },
        {
            'external_strava_id': 'strava_67890',
            'name': 'Rota Parque Ibirapuera',
            'polyline': 'mock_polyline_data_2',
            'color': '#00FF00',
            'distance': '8.2',
            'active': 1
        },
        {
            'external_strava_id': 'strava_54321',
            'name': 'Rota Zona Norte',
            'polyline': 'mock_polyline_data_3',
            'color': '#0000FF',
            'distance': '22.1',
            'active': 1
        }
    ]
    
    for route_data in routes:
        Route.objects.create(**route_data)
    
    print("Routes seeded successfully!")