from django.urls import path
from .views import CityList, CityDetail, HomeData, Event

urlpatterns = [
    path('cities/', CityList.as_view()),
    path('cities/<int:pk>/', CityDetail.as_view()),
    path('home_cities/', HomeData.as_view()),
    path('events/<int:pk>/', Event.as_view()),
]