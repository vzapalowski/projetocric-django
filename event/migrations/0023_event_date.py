# Generated by Django 4.1.7 on 2023-08-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_delete_personaldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, verbose_name='Data do evento'),
        ),
    ]
