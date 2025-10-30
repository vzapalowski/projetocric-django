from django.db.models.signals import pre_save
from django.dispatch import receiver

from event.models import EventImage
from projetocric.utilities import replace

@receiver(pre_save, sender=EventImage)
def change_name_event_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.name = replace(instance.image.name)