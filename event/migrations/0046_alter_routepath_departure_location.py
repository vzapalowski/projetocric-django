# Generated by Django 4.1.7 on 2023-10-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0045_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routepath',
            name='departure_location',
            field=models.CharField(max_length=100, verbose_name='Local de Partida'),
        ),
    ]
