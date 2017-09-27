# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenciaP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='fechaDeNacimiento',
            field=models.DateField(max_length=20),
        ),
    ]
