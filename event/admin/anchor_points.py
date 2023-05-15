from django.contrib import admin

from event.models.anchor_point import AnchorPoint

class AnchorPointAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')

admin.site.register(AnchorPoint, AnchorPointAdmin)