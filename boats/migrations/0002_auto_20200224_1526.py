# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-24 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my.boats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
