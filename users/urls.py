from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_enrollment/<int:enrollment_id>/', views.edit_enrollment, name='edit_enrollment'),
]
