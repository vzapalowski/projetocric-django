# Generated by Django 4.1.7 on 2023-04-14 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0009_alter_city_routes'),
        ('home', '0012_remove_home_banner_photo_city_remove_home_id_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cities.city'),
        ),
    ]