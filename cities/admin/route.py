from django.contrib import admin
from cities.models import Route


class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_route', 'active', 'polyline', 'distance')
    list_display_links = ('id', 'name', 'id_route', 'polyline', 'distance')
    readonly_fields = ('polyline', 'distance')


admin.site.register(Route, RouteAdmin)