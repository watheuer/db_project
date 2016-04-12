# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('win_rate', models.DecimalField(decimal_places=2, max_digits=30)),
                ('kills', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('minions_killed', models.IntegerField()),
                ('q_skill', models.CharField(max_length=32)),
                ('w_skill', models.CharField(max_length=32)),
                ('e_skill', models.CharField(max_length=32)),
                ('r_skill', models.CharField(max_length=32)),
                ('champion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='champion_picker.Champion')),
            ],
        ),
        migrations.CreateModel(
            name='WinRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win_rate', models.DecimalField(decimal_places=2, max_digits=30)),
                ('champ1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='champ1', to='champion_picker.Role')),
                ('champ2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='champ2', to='champion_picker.Role')),
            ],
        ),
    ]
