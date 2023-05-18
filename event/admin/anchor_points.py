from django.contrib import admin

from event.models.anchor_point import AnchorPoint

class AnchorPointAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

admin.site.register(AnchorPoint, AnchorPointAdmin)