# Generated by Django 4.1.7 on 2024-04-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0040_alter_cityimage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='distance',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Distância'),
        ),
    ]
