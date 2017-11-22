# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_user_alias'),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorites', to='login_app.User'),
        ),
    ]