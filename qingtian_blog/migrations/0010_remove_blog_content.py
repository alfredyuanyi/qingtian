# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-07 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qingtian_blog', '0009_auto_20160907_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]
