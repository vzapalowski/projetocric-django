# Generated by Django 4.1.7 on 2023-09-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0036_remove_enrollment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=800, null=True, verbose_name='Descrição do evento'),
        ),
    ]
