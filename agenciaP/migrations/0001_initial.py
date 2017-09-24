# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=8)),
                ('fechaDeNacimiento', models.CharField(max_length=20)),
                ('experienciaLaboral', models.TextField(max_length=200)),
                ('formacion', models.TextField(max_length=200)),
                ('habilidades', models.TextField(max_length=200)),
                ('trabajo', models.TextField(max_length=200, blank=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=200)),
                ('horario', models.CharField(max_length=20)),
                ('profesion', models.CharField(max_length=20)),
            ],
        ),
    ]
