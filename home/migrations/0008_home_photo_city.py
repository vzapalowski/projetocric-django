# Generated by Django 4.1.7 on 2023-04-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_home_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='photo_city',
            field=models.URLField(default=None, editable=False),
        ),
    ]
