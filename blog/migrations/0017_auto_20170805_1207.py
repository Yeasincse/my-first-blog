# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 19:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170805_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 5, 12, 7, 9, 675641)),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_pic',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 5, 12, 7, 9, 675641)),
        ),
    ]
