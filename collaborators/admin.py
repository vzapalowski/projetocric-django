from django.contrib import admin
from .models import Collaborators, URL

class URLInline(admin.TabularInline):
    model = URL
    extra = 1
    max_num = 3

@admin.register(Collaborators)
class CollaboratorsAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")
    list_filter = ("position",)
    inlines = [URLInline]