# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-24 17:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my.boats', '0003_auto_20200224_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='HIN',
            field=models.CharField(error_messages={b'unique': b'This HIN has already been registered.'}, max_length=13, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_HIN', message=b'Invalid HIN.  Please check your HIN.', regex=b'^[a-zA-Z0-9]{12,13}$')]),
        ),
        migrations.AlterField(
            model_name='boat',
            name='year',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code=b'invalid_year', message=b'Year must be a 4-digit number.', regex=b'^[0-9]{4}$')]),
        ),
    ]
