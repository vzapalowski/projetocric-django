# Generated by Django 4.1.7 on 2023-10-04 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0047_extrarouteinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrarouteinfo',
            name='event',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='extra_info', to='event.event'),
            preserve_default=False,
        ),
    ]