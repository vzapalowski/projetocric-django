from django.db import models
from event.models import Event

class EventImage(models.Model):
    PATH_IMAGES_EVENT = 'events/images/%Y/%m/%d'
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image_path = models.ImageField(upload_to=PATH_IMAGES_EVENT)

    def __str__(self):
        return self.image.name

    class Meta:
        db_table = 'event_image'