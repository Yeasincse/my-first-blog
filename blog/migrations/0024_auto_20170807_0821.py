# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 15:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20170806_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 8, 21, 59, 535665)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 8, 21, 59, 535665)),
        ),
    ]
