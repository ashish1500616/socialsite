# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 23:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 23, 17, 17, 617349, tzinfo=utc)),
        ),
    ]