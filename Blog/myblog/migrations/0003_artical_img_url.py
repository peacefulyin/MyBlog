# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20170828_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='img_url',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
