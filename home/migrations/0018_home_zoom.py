# Generated by Django 4.1.7 on 2023-08-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_anchorpointsmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='zoom',
            field=models.IntegerField(default=10),
        ),
    ]
