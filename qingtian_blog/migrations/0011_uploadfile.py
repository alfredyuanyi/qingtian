# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-07 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qingtian_blog', '0010_remove_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HtmlFile', models.FileField(upload_to='templates/')),
            ],
            options={
                'verbose_name': 'html\u6587\u4ef6',
                'verbose_name_plural': 'HTML\u6587\u4ef6',
            },
        ),
    ]
