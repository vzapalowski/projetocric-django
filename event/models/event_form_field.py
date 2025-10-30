from django.db import models
from event.models.event_form import EventForm

class EventFormField(models.Model):
    FORM_TYPES = [
        ("text", "Text"),
        ("number", "Number"),
        ("date", "Date"),
        ("select", "Select"),
        ("file", "File"),
        ("boolean", "Boolean"),
    ]

    form = models.ForeignKey(EventForm, on_delete=models.CASCADE, related_name="fields")
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=FORM_TYPES)
    required = models.BooleanField(default=False)
    options = models.TextField(blank=True, null=True)  # JSON or CSV for select
    order = models.IntegerField(default=0)
    validation = models.TextField(blank=True, null=True)  # regex or rules

    def __str__(self):
        return f"{self.form.name} - {self.name}"

    class Meta:
        db_table = 'event_form_field'
