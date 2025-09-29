from django.contrib import admin
from event.models.anchor_point import AnchorPoint
from event.models.event import Event


class AnchorPointAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
        
admin.site.register(AnchorPoint, AnchorPointAdmin)
