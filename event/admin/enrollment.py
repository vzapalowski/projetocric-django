from django.contrib import admin
from event.models import Enrollment, Bond

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'get_bond_choice_display', 'how_knew', 'rg', 'route')

admin.site.register(Bond)
admin.site.register(Enrollment, EnrollmentAdmin)
