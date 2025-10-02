from django.contrib import admin
from users.models.personal_data import PersonalData
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class PersonalDataInline(admin.StackedInline): 
    model = PersonalData
    can_delete = False
    verbose_name_plural = 'Informações Pessoais'
    
    def has_delete_permission(self, request, obj=None):
        return False

class CustomUserAdmin(UserAdmin):
    inlines = (PersonalDataInline,)

admin.site.unregister(User) 
admin.site.register(User, CustomUserAdmin)
