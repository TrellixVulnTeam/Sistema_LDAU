# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-24 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topico2', '0002_auto_20170623_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agroindustria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidad_produccion', models.CharField(max_length=40)),
                ('tipo', models.CharField(choices=[('ORGANICA', 'organica'), ('JASA', 'jasa'), ('OTRO', 'otro')], default='ORGANICA', max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('asociacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topico2.Asociacion')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topico2.Empresa')),
            ],
            options={
                'verbose_name_plural': 'Agroindustrias',
                'verbose_name': 'Agroindustria',
                'permissions': (('list_agroindustria', 'Can list agroindustria'), ('get_agroindustria', 'Can get agroindustria')),
            },
        ),
    ]
