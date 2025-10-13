from django.db import models
from event.models.enrollment import Enrollment


class EventFormResponse(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="responses")
    field = models.ForeignKey(EventFormField, on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return f"{self.enrollment} - {self.field.name}"

    class Meta:
        db_table = 'event_form_response'