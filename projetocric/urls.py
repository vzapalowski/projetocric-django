from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cidades/', include('cities.urls')),
    path('eventos/', include('event.urls')),
    path('usuarios/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),

    path('reset_password/', user_views.PasswordReset.as_view(), name='reset_password'),
    path('reset_password_sent/', user_views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', user_views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', user_views.PasswordResetComplete.as_view(), name='password_reset_complete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

