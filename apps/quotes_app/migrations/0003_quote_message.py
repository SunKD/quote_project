# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0002_auto_20180323_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='message',
            field=models.TextField(default='just live love laugh', max_length=1000),
            preserve_default=False,
        ),
    ]