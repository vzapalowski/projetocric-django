from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


# faz uma table dos colabs
class Collaborators(models.Model):
    picture = models.ImageField(upload_to='Collaborators/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    is_current = models.BooleanField(default=True, verbose_name='Membro atual do projeto')

    class Meta:
        ordering = ['-is_current', 'name']

    def __str__(self):
        status = "(Atual)" if self.is_current else "(Antigo)"
        return f"{self.name} {status}"

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