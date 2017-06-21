# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('secrets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='secret',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='secret',
            name='like',
            field=models.ManyToManyField(related_name='likes', to='login.User'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
