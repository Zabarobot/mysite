# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20170713_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedition',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
