# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 11:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_auto_20170825_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 25, 19, 7, 56, 938076)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 25, 19, 7, 56, 936075)),
        ),
    ]
