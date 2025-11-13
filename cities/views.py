from django.shortcuts import render
from django.views.generic.detail import DetailView
from cities.models import City
from core.models import AnchorpointCategory
from event.models import Event
from api.mixins import ApiTokenMixin


class CityDetail(ApiTokenMixin ,DetailView):
    model = City
    template_name = 'cities/city_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.get_object()
        
        images = []
        for index, image in enumerate(city.images.all()):
            is_even = (index % 2 == 0)
            images.append({
                'url': image.image_path.url,
                'title': image.title,
                'subtitle': image.subtitle,
                'is_even': is_even
            })
        
        context['images'] = images
        
        try:
            context['events'] = Event.objects.filter(city=city)
        except:
            context['events'] = Event.objects.all()
        
        context['categories_points'] = AnchorpointCategory.objects.all()
        
        return context