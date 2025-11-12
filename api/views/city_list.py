from rest_framework import generics
from cities.models import City
from api.serializers import CitySerializer
from api.permissions import HasApiAuthToken

class CityList(generics.ListAPIView):
    permission_classes = [HasApiAuthToken]
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.filter(visible=True)
        return queryset
    