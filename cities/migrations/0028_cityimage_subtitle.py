# Generated by Django 4.1.7 on 2023-06-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0027_cityimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityimage',
            name='subtitle',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]