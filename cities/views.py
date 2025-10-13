from django.shortcuts import render
from django.views.generic.detail import DetailView
from cities.models import City
from core.models import AnchorpointCategory
from event.models import Event


class CityDetail(DetailView):
    model = City
    template_name = 'cities/city_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = City.objects.get(pk=self.kwargs['pk'])
        context['city'] = city
        images = []
        for index, image in enumerate(city.images.all()):
            is_even = (index % 2 == 0)
            images.append((image.image.url, image.tittle, image.subtitle, is_even))
        context['images'] = images
        context['events'] = Event.objects.all()
        context['categories_points'] = Category.objects.all()

        return context
    