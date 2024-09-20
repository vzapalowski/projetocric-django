# Generated by Django 4.1.7 on 2024-09-20 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/images/%Y/%m/%d')),
                ('social_network', models.CharField(blank=True, max_length=30, null=True, verbose_name='Instagram')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Data de Nascimento')),
                ('rg', models.CharField(max_length=10, null=True, verbose_name='RG')),
                ('bond_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.bond', verbose_name='Vínculo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
