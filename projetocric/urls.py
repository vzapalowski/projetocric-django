
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from api.views import RouteViewSet

routes = routers.DefaultRouter()

routes.register(r'routes', RouteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('cidades/', include('cities.urls')),
    path('sobre/', include('about.urls')),
    path('manual/', include('manual.urls')),
    path('contato/', include('contact.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(routes.urls))
]
