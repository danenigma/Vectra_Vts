# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-10 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectra_vts', '0002_auto_20170110_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='plate_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
