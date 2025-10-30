from django.contrib import admin
from users.models.user_profile import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserProfileInline(admin.StackedInline): 
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Informações Pessoais'
    
    def has_delete_permission(self, request, obj=None):
        return False

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, ) if hasattr(__name__, 'UserProfileInline') else ()

admin.site.unregister(User) 
admin.site.register(User, CustomUserAdmin)
