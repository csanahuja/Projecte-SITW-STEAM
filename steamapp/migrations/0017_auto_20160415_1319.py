# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steamapp', '0016_auto_20160415_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownedachievement',
            old_name='apiname',
            new_name='achid',
        ),
        migrations.AlterUniqueTogether(
            name='ownedachievement',
            unique_together=set([('steamid', 'achid')]),
        ),
    ]
