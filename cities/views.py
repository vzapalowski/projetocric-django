from django.shortcuts import render
from django.views.generic.detail import DetailView
from cities.models import City


class CityDetail(DetailView):
    model = City
    template_name = 'cities/city_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(pk=self.kwargs['pk'])
        return context
    