# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 15:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170804_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 15, 15, 58, 554050, tzinfo=utc)),
        ),
    ]
