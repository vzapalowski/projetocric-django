from django.contrib import admin
from event.models import EnrollmentFormType2, EnrollmentType2


class EnrollmentType2Admin(admin.ModelAdmin):
    form = EnrollmentFormType2
    fields = ('full_name', 'email', 'event')

admin.site.register(EnrollmentType2, EnrollmentType2Admin)
