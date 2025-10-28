from django.urls import path
from . import views


app_name = 'events'
urlpatterns = [
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # path('<int:event_id>/enrollment/', views.enrollment, name='enrollment'),
    # path('<int:event_id>/enrollment2/', views.enrollment2, name='enrollment2'),
    # path('<int:event_id>/enrollment3/', views.enrollment3, name='enrollment3'),
    # path('<int:event_id>/enrollment4/', views.enrollment4, name='enrollment4'),
    path('<int:event_id>/download/', views.download_pdf, name='download_pdf'),
    # path('<int:enrollment_id>/delete_enrollment/', views.delete_enrollment, name='delete_enrollment'),
    # path('<int:enrollment_id>/delete_enrollment_type2/', views.delete_enrollment_type2, name='delete_enrollment_type2'),
    # path('<int:enrollment_id>/delete_enrollment_type3/', views.delete_enrollment_type3, name='delete_enrollment_type3'),
    # path('<int:enrollment_id>/delete_enrollment_type4/', views.delete_enrollment_type4, name='delete_enrollment_type4'),
    # path('<int:enrollment_id>/get_certificate/', views.get_certificate, name='get_certificate')
]
