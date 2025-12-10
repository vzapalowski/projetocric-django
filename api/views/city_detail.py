from rest_framework import generics
from api.serializers import CityDetailSerializer
from cities.models import City
from api.permissions import HasApiAuthToken

class CityDetail(generics.RetrieveAPIView):
    permission_classes = [HasApiAuthToken]
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = City.objects.filter(visible=True)
        return queryset
    