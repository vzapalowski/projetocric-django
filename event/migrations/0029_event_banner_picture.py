# Generated by Django 4.1.7 on 2023-09-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0028_event_zoom'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='banner_picture',
            field=models.ImageField(blank=True, null=True, upload_to='events/images/%Y/%m/%d'),
        ),
    ]
