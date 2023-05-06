from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.CityDetail.as_view(), name='city_detail'),
]