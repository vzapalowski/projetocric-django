# Generated by Django 4.1.7 on 2023-04-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0008_alter_city_routes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='routes',
            field=models.ManyToManyField(blank=True, null=True, to='cities.route'),
        ),
    ]
