from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.PostHome.as_view(), name='home'),
]
