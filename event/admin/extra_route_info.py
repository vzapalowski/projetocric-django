from django.contrib import admin
from event.models.extra_route_info import ExtraRouteInfo


class ExtraRouteInfoAdmin(admin.StackedInline):
    model = ExtraRouteInfo

# admin.site.register(ExtraRouteInfo)