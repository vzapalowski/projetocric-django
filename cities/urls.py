from django.urls import path
from . import views

urlpatterns = [
    path('charqueadas/', views.charqueadas),
    path('valeVerde/', views.valeVerde)
]