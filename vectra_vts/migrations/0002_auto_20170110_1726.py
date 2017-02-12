# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-10 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectra_vts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='engine',
            new_name='brand_name',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_type',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='made_year',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='maker',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='net_weight',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine_cc',
            field=models.CharField(default='', max_length=50),
        ),
    ]
