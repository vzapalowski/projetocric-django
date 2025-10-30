from django.db import models

class EventHowknew(models.Model):
    code_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Código de nome')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Como soube ?')

    def __str__(self):
        return self.code_name

    class Meta:
        db_table = 'event_howknew'