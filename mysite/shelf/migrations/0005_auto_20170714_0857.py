# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20170713_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editions', to='shelf.Book'),
        ),
    ]
