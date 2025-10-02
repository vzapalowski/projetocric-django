from django.contrib import admin
from event.models import HowKnew
from event.models.event import Event



class HowKnewAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name']
        
admin.site.register(HowKnew, HowKnewAdmin)
