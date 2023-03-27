from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostHome.as_view(), name='home')
]