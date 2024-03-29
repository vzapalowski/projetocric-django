# Generated by Django 4.2 on 2023-04-24 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0012_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=100)),
                ('number', models.PositiveSmallIntegerField()),
                ('neighboorhood', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city')),
            ],
        ),
        migrations.CreateModel(
            name='AnchorPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=20)),
                ('business_hours', models.CharField(max_length=120)),
                ('phone', models.PositiveSmallIntegerField(default='(51) ')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.category')),
            ],
        ),
    ]
