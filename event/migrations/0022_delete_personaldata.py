# Generated by Django 4.1.7 on 2023-08-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0021_remove_personaldata_full_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalData',
        ),
    ]
