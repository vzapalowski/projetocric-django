from django.db import models

class EventBond(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Vínculo')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'event_bond'