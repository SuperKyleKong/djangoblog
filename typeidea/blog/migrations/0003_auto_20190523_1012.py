# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 02:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]
