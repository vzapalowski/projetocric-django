from django.db import models

class EventHowknew(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Como soube ?')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'event_howknew'