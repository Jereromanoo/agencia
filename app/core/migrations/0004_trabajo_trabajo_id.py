# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_trabajo_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='trabajo_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
