from django.contrib import admin
from .models import Collaborators, URL

class URLInline(admin.TabularInline):
    model = URL
    extra = 1
    max_num = 3

@admin.register(Collaborators)
class CollaboratorsAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "is_current_status")
    search_fields = ("name", "position")
    list_filter = ("position", "is_current")
    fieldsets = (
        ("Informações Pessoais", {
            "fields": ("name", "position", "picture")
        }),
        ("Status", {
            "fields": ("is_current",),
            "description": "Marque se este colaborador está atualmente no projeto ou se é um integrante antigo."
        }),
    )
    inlines = [URLInline]

    def is_current_status(self, obj):
        if obj.is_current:
            return "✓ Atual"
        else:
            return "✗ Antigo"
    is_current_status.short_description = "Status"