# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 18:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20170825_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 25, 2, 16, 15, 551158)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 25, 2, 16, 15, 550159)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='edit_status',
            field=models.BooleanField(default=False),
        ),
    ]
