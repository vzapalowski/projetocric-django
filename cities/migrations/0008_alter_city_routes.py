# Generated by Django 4.1.7 on 2023-04-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0007_remove_city_id_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='routes',
            field=models.ManyToManyField(blank=True, to='cities.route'),
        ),
    ]
