# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champion_picker', '0002_auto_20160413_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='e_skill',
        ),
        migrations.RemoveField(
            model_name='role',
            name='q_skill',
        ),
        migrations.RemoveField(
            model_name='role',
            name='r_skill',
        ),
        migrations.RemoveField(
            model_name='role',
            name='w_skill',
        ),
        migrations.AddField(
            model_name='champion',
            name='e_skill',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='champion',
            name='q_skill',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='champion',
            name='r_skill',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='champion',
            name='w_skill',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
