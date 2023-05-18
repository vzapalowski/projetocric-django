from django.views.generic.list import ListView

from home.models import CityManager
from cities.models import City
from cities.models import Category
from event.models import Event

class PostHome(ListView):
    template_name = 'home/index.html'
    model = City

    def get_queryset(self):
        return City.objects.filter(visible=True).select_related('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = CityManager.objects.all()
        context['categories_points'] = Category.objects.all()
        context['events'] = Event.objects.all()
        return context
