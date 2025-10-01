from django.contrib import admin
from .enrollment import EnrollmentAdmin
from event.models import Enrollment3PasseioCiclistico
from ..models.enrollment_3_passeio_ifsul_form import enrollment3PasseioIfsulForm

class Enrollment3PasseioCiclisticoAdmin(EnrollmentAdmin):
    form = enrollment3PasseioIfsulForm
    
admin.site.register(Enrollment3PasseioCiclistico, Enrollment3PasseioCiclisticoAdmin)
