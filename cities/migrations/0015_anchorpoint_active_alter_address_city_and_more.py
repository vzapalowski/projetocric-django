# Generated by Django 4.2 on 2023-04-25 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0014_rename_neighboorhood_address_neighborhood_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anchorpoint',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city', verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='address',
            name='neighborhood',
            field=models.CharField(max_length=100, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.PositiveSmallIntegerField(verbose_name='Número do comércio'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(max_length=100, verbose_name='Nome da rua'),
        ),
        migrations.AlterField(
            model_name='anchorpoint',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.address', verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='anchorpoint',
            name='business_hours',
            field=models.CharField(max_length=120, verbose_name='Horário de funcionamento'),
        ),
        migrations.AlterField(
            model_name='anchorpoint',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.category', verbose_name='Tipo do comérico'),
        ),
        migrations.AlterField(
            model_name='anchorpoint',
            name='lat',
            field=models.CharField(max_length=20, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='anchorpoint',
            name='lng',
            field=models.CharField(max_length=20, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='anchorpoint',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='anchorpoint',
            name='phone',
            field=models.CharField(default='(51) ', max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='city',
            name='lat',
            field=models.CharField(default='-29.95', max_length=50, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='city',
            name='lng',
            field=models.CharField(default='-51.64', max_length=50, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='city',
            name='points',
            field=models.ManyToManyField(blank=True, null=True, to='cities.anchorpoint', verbose_name='Pontos de apoio'),
        ),
        migrations.AlterField(
            model_name='city',
            name='routes',
            field=models.ManyToManyField(blank=True, null=True, to='cities.route', verbose_name='Rotas'),
        ),
        migrations.AlterField(
            model_name='route',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Ativa'),
        ),
        migrations.AlterField(
            model_name='route',
            name='id_route',
            field=models.CharField(max_length=50, unique=True, verbose_name='Id da rota'),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='route',
            name='polyline',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Marcação'),
        ),
    ]
