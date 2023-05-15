from django.contrib import admin

from event.models import Event
from event.admin.event_form import EventForm
from event.admin.image import ImageAdmin
from event.models.anchor_point import AnchorPoint
from event.models.route_path import RoutePath

class EventAdmin(admin.ModelAdmin):
    form = EventForm
    inlines = [ImageAdmin]
    list_display = ('id', 'description')
    list_display_links = ('id', 'description')

    class Meta:
        model = Event

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "routes_data":
            kwargs["queryset"] = RoutePath.objects.filter(active=True)
        
        if db_field.name == "points":
            kwargs["queryset"] = AnchorPoint.objects.filter(active=True)

        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Event, EventAdmin)
