# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]