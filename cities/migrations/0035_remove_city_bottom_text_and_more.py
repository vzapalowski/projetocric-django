# Generated by Django 4.1.7 on 2023-07-18 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0034_alter_city_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='bottom_text',
        ),
        migrations.RemoveField(
            model_name='city',
            name='bottom_text_tittle',
        ),
    ]