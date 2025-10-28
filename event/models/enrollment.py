from django.db import models
from event.models import EventRoute
from event.models.event import Event
from django.contrib.auth.models import User

    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    route = models.ForeignKey(EventRoute, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

    class Meta:
        db_table = 'event_enrollment'
        unique_together = ('event', 'user')