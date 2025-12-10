from django.views.generic.list import ListView

from home.models import CityManager
from cities.models import City
from core.models import AnchorpointCategory
from event.models import Event
from api.mixins import ApiTokenMixin
class Home(ApiTokenMixin, ListView):
    template_name = 'home/index.html'
    model = City

    def get_queryset(self):
        return City.objects.filter(visible=True).select_related('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = CityManager.objects.all()
        context['categories_points'] = AnchorpointCategory.objects.all()
        events = Event.objects.order_by('status')

        for event in events:
            event.number_of_routes = event.routes.count()
            event.participants_count = event.participants.count()
        
        context['events'] = events
        return context
