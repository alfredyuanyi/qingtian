# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-20 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(default='\u8bb8\u5065', max_length=20)),
                ('content', models.TextField()),
                ('blog_type', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('traffic', models.IntegerField(default=0)),
                ('approval', models.IntegerField(default=0)),
                ('oppostion', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-traffic'],
                'verbose_name': '\u535a\u5ba2',
            },
        ),
    ]