# Generated by Django 4.1.7 on 2023-04-11 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0008_alter_city_routes'),
        ('home', '0004_delete_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name_city', models.CharField(editable=False, max_length=100, verbose_name='Nome da Cidade')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city')),
            ],
        ),
    ]
