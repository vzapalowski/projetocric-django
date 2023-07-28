from django.contrib import admin
from cities.models import Route


class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_route', 'active', 'polyline')
    list_display_links = ('id', 'name', 'id_route', 'polyline')
    readonly_fields = ('polyline',)


admin.site.register(Route, RouteAdmin)
