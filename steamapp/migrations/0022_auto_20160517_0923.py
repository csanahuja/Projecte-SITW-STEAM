# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steamapp', '0021_auto_20160510_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ban',
            name='steamid',
        ),
        migrations.DeleteModel(
            name='Ban',
        ),
    ]
