from rest_framework import generics
from api.serializers import EventSerializer
from event.models import Event


class Event(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'
    