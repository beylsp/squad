# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-23 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_populate_status_has_metrics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knownissue',
            old_name='environment',
            new_name='environments',
        ),
    ]
