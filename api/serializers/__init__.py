# api/serializers/__init__.py
from .route import RouteSerializer
from .anchorpoint import AnchorpointSerializer
from .anchorpoint_category import AnchorpointCategorySerializer
from .event import EventSerializer
from .event_route import EventRouteSerializer
from .city import CitySerializer

# Import CityDetailSerializer separadamente para evitar circularidade
try:
    from .city_detail import CityDetailSerializer
except ImportError:
    # Fallback para evitar problemas de importação circular
    CityDetailSerializer = None

__all__ = [
    'RouteSerializer', 
    'AnchorpointSerializer', 
    'AnchorpointCategorySerializer',
    'EventSerializer', 
    'EventRouteSerializer', 
    'CitySerializer',
    'CityDetailSerializer'
]