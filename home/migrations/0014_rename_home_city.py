# Generated by Django 4.1.7 on 2023-04-18 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0010_city_lat_city_lng'),
        ('home', '0013_alter_home_city'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Home',
            new_name='City',
        ),
    ]