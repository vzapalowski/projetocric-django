# Generated by Django 4.1.7 on 2023-08-09 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0019_remove_personaldata_email_personaldata_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='bond_choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event.bond', verbose_name='Vínculo'),
            preserve_default=False,
        ),
    ]
