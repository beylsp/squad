# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-27 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0099_metricthreshold'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='is_outlier',
            field=models.BooleanField(default=False),
        ),
    ]