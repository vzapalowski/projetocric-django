from django.db import models

class Segment(models.Model):
    id = models.CharField(max_length=50, primary_key=True, verbose_name='Id do Segmento')
    name = models.CharField(max_length=250, verbose_name='Nome do Segmento')
    city = models.CharField(max_length=250, default="Não Informada", null=True, verbose_name='Cidade')
    state = models.CharField(max_length=250, default="Não Informado", null=True, verbose_name='Estado')
    country = models.CharField(max_length=250, default="Não Informado", null=True, verbose_name='País')
    distance = models.CharField(max_length=250, default="Não Informada", null=True, verbose_name='Distância')
    total_elevation_gain = models.CharField(max_length=250, default="Não Informado", null=True, verbose_name='Ganho de Elevação')
    average_grade = models.CharField(max_length=250, default="Não Informada", null=True, verbose_name='Inclinação Média')
    elevation_low = models.CharField(max_length=250, default="Não Informada", null=True, verbose_name='Elevação Mínima')
    elevation_high = models.CharField(max_length=250, default="Não Informada", null=True, verbose_name='Elevação Máxima')
    effort_count = models.CharField(max_length=250, default="Não Informadas", null=True, verbose_name='Tentativas')
    athlete_count = models.CharField(max_length=250, default="Não Informada", null=True, verbose_name='Contagem de Atletas')
    polyline = models.CharField(max_length=5000, default="Não Informada", null=True, verbose_name='Marcação')
    route = models.ForeignKey('Route', on_delete=models.CASCADE, related_name='segments', verbose_name='Rota')
    visible = models.BooleanField(default=True, verbose_name='Visível')  # Novo campo

    def __str__(self):
        return f"{self.name} (ID: {self.id})"