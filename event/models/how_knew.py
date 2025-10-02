from django.db import models

class HowKnew(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Como soube ?')

    def __str__(self):
        return self.name