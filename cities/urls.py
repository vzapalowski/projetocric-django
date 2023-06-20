from django.urls import path
from . import views


app_name = 'cities'
urlpatterns = [
    path('<int:pk>/', views.CityDetail.as_view(), name='city_detail'),
]
