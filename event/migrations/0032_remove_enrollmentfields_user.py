# Generated by Django 4.1.7 on 2023-09-19 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0031_enrollmentfields_event_enrollment_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollmentfields',
            name='user',
        ),
    ]
