# Generated by Django 4.1.7 on 2023-06-14 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_alter_warning_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event.event', verbose_name='Evento'),
            preserve_default=False,
        ),
    ]
