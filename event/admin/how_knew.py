from django.contrib import admin
from event.models import HowKnew

class HowKnewAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name']

admin.site.register(HowKnew, HowKnewAdmin)