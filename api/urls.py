from django.urls import path
from .views import CityList, CityDetail, HomeData, EventDetails, EventList


urlpatterns = [
    path('cities/', CityList.as_view()),
    path('cities/<int:pk>/', CityDetail.as_view()),
    path('home_cities/', HomeData.as_view()),
    path('event_list/', EventList.as_view()),
    path('events/<int:pk>/', EventDetails.as_view()),
]
