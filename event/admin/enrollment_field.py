from django.contrib import admin
from event.models.enrollment_field import EnrollmentField


class EnrollmentFieldAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name']

admin.site.register(EnrollmentField, EnrollmentFieldAdmin)