from rest_framework import generics
from api.serializers import EventSerializer
from event.models import Event
from api.permissions import HasApiAuthToken

class EventList(generics.ListAPIView):
    permission_classes = [HasApiAuthToken]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetails(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'
