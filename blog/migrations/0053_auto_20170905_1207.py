# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 12:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0052_auto_20170905_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 12, 7, 4, 158917)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 12, 7, 4, 157468)),
        ),
    ]