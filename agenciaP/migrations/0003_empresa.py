# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenciaP', '0002_auto_20170927_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('cuit', models.CharField(max_length=11)),
                ('razonSocial', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=25)),
                ('logo', models.ImageField(upload_to=b'static/images')),
                ('rubro', models.CharField(max_length=20)),
            ],
        ),
    ]
