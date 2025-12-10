from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


# faz uma table dos colabs
class Collaborators(models.Model):
    picture = models.ImageField(upload_to='Collaborators/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class URL(models.Model):
    collaborator = models.ForeignKey(Collaborators, on_delete=models.CASCADE, related_name='urls')
    url = models.URLField(max_length=600, blank=True)

#popular o banco com os devs pelo seed
@receiver(post_migrate)
def seed_data(sender, **kwargs):
    if sender.label == 'collaborators':
    
        if Collaborators.objects.exists():
            return
        from .seed import run
        run()