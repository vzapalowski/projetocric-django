from django.urls import path
from . import views

urlpatterns = [
    path('charqueadas/', views.charqueadas, name='cidade/charqueadas'),
    path('vale_verde/', views.vale_verde, name='cidade/vale_verde'),
]