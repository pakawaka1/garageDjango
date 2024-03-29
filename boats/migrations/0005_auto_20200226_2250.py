# Generated by Django 3.0.3 on 2020-02-26 22:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my.boats', '0004_auto_20200224_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='HIN',
            field=models.CharField(error_messages={'unique': 'This HIN has already been registered.'}, max_length=13, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_HIN', message='Invalid HIN.  Please check your HIN.', regex='^[a-zA-Z0-9]{12,13}$')]),
        ),
        migrations.AlterField(
            model_name='boat',
            name='year',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_year', message='Year must be a 4-digit number.', regex='^[0-9]{4}$')]),
        ),
    ]
