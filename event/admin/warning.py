from django.contrib import admin

from event.models.warning import Warning

class WarningAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title', 'content')

admin.site.register(Warning, WarningAdmin)