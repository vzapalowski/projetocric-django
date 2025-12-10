from django.db import models

class EventBond(models.Model):
    code_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Código de nome')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Vínculo')

    def __str__(self):
        return self.code_name

    class Meta:
        db_table = 'event_bond'
        verbose_name = 'Vínculo'
        verbose_name_plural = 'Vínculos'