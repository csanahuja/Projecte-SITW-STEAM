# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steamapp', '0008_auto_20160408_1303'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ownedgame',
            unique_together=set([('steamid', 'appid')]),
        ),
    ]