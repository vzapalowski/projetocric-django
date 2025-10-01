from django.contrib import admin
from .enrollment import EnrollmentAdmin
from event.models import Enrollment4PasseioCiclistico
from ..models.enrollment_4_passeio_ifsul_form import enrollment4PasseioIfsulForm

class Enrollment4PasseioCiclisticoAdmin(EnrollmentAdmin):
    form = enrollment4PasseioIfsulForm
    
admin.site.register(Enrollment4PasseioCiclistico, Enrollment4PasseioCiclisticoAdmin)
