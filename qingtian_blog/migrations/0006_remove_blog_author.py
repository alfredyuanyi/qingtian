# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-20 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qingtian_blog', '0005_auto_20160720_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
