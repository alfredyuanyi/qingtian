# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-20 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qingtian_blog', '0002_auto_20160720_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(default='\u8bb8\u5065', max_length=20),
        ),
    ]
