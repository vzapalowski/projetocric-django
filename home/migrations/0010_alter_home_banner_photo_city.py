# Generated by Django 4.1.7 on 2023-04-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_photo_city_home_banner_photo_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='banner_photo_city',
            field=models.URLField(default=None, editable=False, verbose_name='Imagem do Banner'),
        ),
    ]
