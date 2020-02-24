# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-24 15:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my.cars', '0002_auto_20200224_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='VIN',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_VIN', message=b'VIN must be alphanumeric.', regex=b'^[a-zA-Z0-9]*$')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='currentMileage',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='nextService',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='seats',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='serviceInterval',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
