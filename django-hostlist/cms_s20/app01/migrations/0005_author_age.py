# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-17 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20180515_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
