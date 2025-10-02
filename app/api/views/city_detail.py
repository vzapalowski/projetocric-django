from rest_framework import generics
from api.serializers import CityDetailSerializer
from cities.models import City


class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = City.objects.filter(visible=True)
        return queryset
    