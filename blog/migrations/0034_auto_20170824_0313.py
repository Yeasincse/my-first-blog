# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 19:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20170823_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='edit_status',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 3, 13, 58, 427781)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 3, 13, 58, 427781)),
        ),
    ]
