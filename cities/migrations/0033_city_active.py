# Generated by Django 4.1.7 on 2023-07-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0032_cityimage_tittle'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Estado da cidade'),
        ),
    ]
