from django.contrib import admin
from event.models.route_path import RoutePath

class RoutePathAdmin(admin.ModelAdmin):
    list_display = ('name', 'route', 'time', 'departure_location',)
    list_display_links = ('name', 'route', 'time', 'departure_location',)
    ordering = ['name']

admin.site.register(RoutePath, RoutePathAdmin)