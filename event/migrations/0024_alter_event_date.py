# Generated by Django 4.1.7 on 2023-08-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0023_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Data do evento'),
        ),
    ]