# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrganiseLunch', '0002_auto_20170504_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='orders',
        ),
        migrations.AddField(
            model_name='meal',
            name='slack_channel',
            field=models.CharField(default='LunchHack', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='meal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='OrganiseLunch.Meal'),
            preserve_default=False,
        ),
    ]
