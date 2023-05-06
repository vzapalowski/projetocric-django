from django.urls import path
from . import views


app_name = 'events'
urlpatterns = [
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    path('<int:event_id>/enrollment/', views.enrollment, name='enrollment'),
]