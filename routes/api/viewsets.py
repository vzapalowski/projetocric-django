from rest_framework import viewsets
from routes.api import serializers
from routes import models

class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RouteSerializer
    queryset = models.Route.objects.all()