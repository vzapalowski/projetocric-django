# Generated by Django 4.1.7 on 2023-05-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routepath',
            name='time',
            field=models.CharField(max_length=30, verbose_name='Horário de Sáida'),
        ),
    ]
