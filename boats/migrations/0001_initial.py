# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-24 05:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(error_messages={b'blank': b'Enter a make.', b'invalid': b'Make must not have more than 20 characters.'}, max_length=20)),
                ('model', models.CharField(error_messages={b'blank': b'Enter a model.', b'invalid': b'Model must not have more than 20 characters.'}, max_length=20)),
                ('year', models.CharField(error_messages={b'blank': b'Enter a year.', b'invalid': b'Year must have 4 characters.'}, max_length=4)),
                ('length', models.CharField(error_messages={b'blank': b'Enter the length.', b'invalid': b'Length must not have more than 20 characters.'}, max_length=20)),
                ('width', models.CharField(error_messages={b'blank': b'Enter the width.', b'invalid': b'Width must not have more than 20 characters.'}, max_length=20)),
                ('HIN', models.CharField(error_messages={b'blank': b'Enter a HIN.', b'invalid': b'Enter a valid HIN.'}, max_length=13, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_HIN', message=b'HIN must be alphanumeric.', regex=b'^[a-zA-Z0-9]*$')])),
                ('currentHours', models.CharField(error_messages={b'blank': b'Enter the current mileage.', b'invalid': b'Current hours must not have more than 7 characters.'}, max_length=7)),
                ('serviceInterval', models.CharField(error_messages={b'blank': b'Enter the service interval.', b'invalid': b'Service internal must not have more than 50 characters.'}, max_length=50)),
                ('nextService', models.CharField(error_messages={b'blank': b'Enter the service interval.', b'invalid': b'Service internal must not have more than 50 characters.'}, max_length=50)),
            ],
        ),
    ]
