# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monyong', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='log',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('S', 'Start'), ('D', 'Done'), ('X', 'Cancel')], default='S', max_length=1),
        ),
    ]