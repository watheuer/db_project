# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('champion_picker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
            ],
        ),
        migrations.AddField(
            model_name='champion',
            name='portrait_image',
            field=models.ImageField(blank=True, null=True, upload_to='champ_images'),
        ),
        migrations.AddField(
            model_name='itembuild',
            name='champion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='champion_picker.Champion'),
        ),
        migrations.AddField(
            model_name='itembuild',
            name='items',
            field=models.ManyToManyField(related_name='items', to='champion_picker.Item'),
        ),
    ]