# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-14 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_authordetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='poll_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]
