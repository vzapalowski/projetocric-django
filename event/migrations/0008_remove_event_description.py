# Generated by Django 4.2 on 2023-05-02 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
    ]
