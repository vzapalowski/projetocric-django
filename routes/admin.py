from django.contrib import admin
from .models import Route

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_route', 'polilyne')
    list_display_links = ('id', 'name')

admin.site.register(Route, RouteAdmin)
