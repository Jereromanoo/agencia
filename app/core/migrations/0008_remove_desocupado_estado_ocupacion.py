# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171110_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desocupado',
            name='estado_ocupacion',
        ),
    ]