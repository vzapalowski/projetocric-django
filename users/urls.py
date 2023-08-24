from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('upload_image/', views.upload_image, name='upload_image'),
]
