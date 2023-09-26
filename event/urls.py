from django.urls import path
from . import views


app_name = 'events'
urlpatterns = [
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    path('<int:event_id>/enrollment/', views.enrollment, name='enrollment'),
    path('<int:event_id>/enrollment2/', views.enrollment2, name='enrollment2'),
    path('<int:event_id>/download/', views.download_pdf, name='download_pdf')
]