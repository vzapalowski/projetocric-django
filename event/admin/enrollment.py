from django.contrib import admin
from event.models import Enrollment, Bond
from .enrollmentform import EnrollmentForm

from event.models.route_path import RoutePath


class BondAdmin(admin.ModelAdmin):
    ordering = ['name']

class EnrollmentAdmin(admin.ModelAdmin):
    form = EnrollmentForm
    list_display = ('full_name', 'date_of_birth', 'how_knew', 'rg',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "route_path":
            kwargs["queryset"] = RoutePath.objects.filter(active=True)
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Bond, BondAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
