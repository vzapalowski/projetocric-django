# Generated by Django 4.1.7 on 2024-09-21 02:15

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0025_remove_route_color_alter_route_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None, verbose_name='Cor da rota'),
        ),
        migrations.AlterField(
            model_name='route',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Ativa'),
        ),
        migrations.AlterField(
            model_name='route',
            name='distance',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Distância'),
        ),
        migrations.AlterField(
            model_name='route',
            name='id_route',
            field=models.CharField(max_length=50, unique=True, verbose_name='Id da rota'),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='route',
            name='polyline',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Marcação'),
        ),
    ]
