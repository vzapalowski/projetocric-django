from django.contrib import admin

from event.models import Event
from event.admin.event_form import EventForm
from cities.models import Route
from event.admin.image import ImageAdmin

class EventAdmin(admin.ModelAdmin):
    form = EventForm
    inlines = [ImageAdmin]
    list_display = ('id', 'description')
    list_display_links = ('id', 'description')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "routes":
            kwargs["queryset"] = Route.objects.filter(active=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    
    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)

