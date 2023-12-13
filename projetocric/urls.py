from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cidades/', include('cities.urls')),
    path('eventos/', include('event.urls')),
    path('usuarios/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html',
    email_template_name='users/custom_password_reset_email.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/reset.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'), name='password_reset_complete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

