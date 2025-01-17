# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-24 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
        ('topico2', '0004_auto_20170624_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_certificadora', models.CharField(max_length=40)),
                ('area_cosechada', models.IntegerField(blank=True, null=True)),
                ('area_perdida', models.IntegerField(blank=True, null=True)),
                ('area_sembrada', models.IntegerField(blank=True, null=True)),
                ('area_total_produccion', models.IntegerField(blank=True, null=True)),
                ('area_total_terreno', models.IntegerField(blank=True, null=True)),
                ('cetificacion_organica', models.BooleanField(default=True)),
                ('tipo', models.CharField(choices=[('CONVENCIONAL', 'convencional'), ('ORGANICO', 'organico')], default='CONVENCIONAL', max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': (('list_produccion', 'Can list produccion'), ('get_produccion', 'Can get produccion')),
                'verbose_name': 'Produccion',
                'verbose_name_plural': 'Produccions',
            },
        ),
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencia_agraria', models.CharField(max_length=40)),
                ('comunidad', models.CharField(max_length=40)),
                ('ruc', models.IntegerField(blank=True, null=True)),
                ('sector', models.CharField(max_length=40)),
                ('Representante', models.BooleanField(default=False)),
                ('tipo', models.CharField(choices=[('GERENTE_ADMINISTRATIVO', 'gerente_administrativo'), ('GERENTE_COMERCIAL', 'gerente_comercial'), ('GERENTE_GENERAL', 'gerente_general'), ('GERENTE_OPERACIONES', 'gerente_operaciones'), ('GERENTE_PRODUCCION', 'gerente_produccion'), ('PRESIDENTE', 'presidente'), ('OTROS', 'otros')], default='GERENTE_ADMINISTRATIVO', max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auths.Person')),
            ],
            options={
                'permissions': (('list_productor', 'Can list productor'), ('get_productor', 'Can get productor')),
                'verbose_name': 'Productor',
                'verbose_name_plural': 'Productors',
            },
        ),
        migrations.CreateModel(
            name='Variedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('cosechas', models.IntegerField(blank=True, null=True)),
                ('production', models.IntegerField(blank=True, null=True)),
                ('siembra', models.IntegerField(blank=True, null=True)),
                ('superficie_perdida', models.IntegerField(blank=True, null=True)),
                ('superficie_verde', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': (('list_variedad', 'Can list variedad'), ('get_variedad', 'Can get variedad')),
                'verbose_name': 'Variedad',
                'verbose_name_plural': 'Variedads',
            },
        ),
        migrations.AddField(
            model_name='asociacion',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topico2.Producto'),
        ),
        migrations.AddField(
            model_name='produccion',
            name='variedad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topico2.Variedad'),
        ),
        migrations.AddField(
            model_name='asociacion',
            name='produccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topico2.Produccion'),
        ),
        migrations.AddField(
            model_name='asociacion',
            name='productor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topico2.Productor'),
        ),
    ]
