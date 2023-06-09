from django.contrib import admin
from event.models import Enrollment, Bond
from ..models.enrollmentform import EnrollmentForm
from event.models.route_path import RoutePath
import csv
from django.http import HttpResponse


class BondAdmin(admin.ModelAdmin):
    ordering = ['name']

class EnrollmentAdmin(admin.ModelAdmin):
    form = EnrollmentForm
    list_display = ('full_name', 'date_of_birth', 'how_knew', 'rg', 'route_path')
    actions = ['export_enrollments_to_csv']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "route_path":
            kwargs["queryset"] = RoutePath.objects.filter(active=True)
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def export_enrollments_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="enrollments.csv"'

        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Email', 'Instagram', 'Date of Birth', 'Category', 'How Knew', 'RG', 'Route Path'])

        for enrollment in queryset:
            writer.writerow([
                enrollment.full_name,
                enrollment.email,
                enrollment.social_network,
                enrollment.date_of_birth,
                enrollment.bond_choice.name,
                enrollment.how_knew.name,
                enrollment.rg,
                enrollment.route_path.name
            ])

        return response

    export_enrollments_to_csv.short_description = 'Export selected enrollments to CSV'


admin.site.register(Bond, BondAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
