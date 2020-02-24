from django.db import models
from django.core.validators import RegexValidator

class Truck(models.Model):
    make = models.CharField(max_length=20,
        error_messages = {
            'invalid': 'Make must not have more than 20 characters.',
            'blank': 'Enter a make.'
        }
    )
    model = models.CharField(max_length=20,
        error_messages = {
            'invalid': 'Model must not have more than 20 characters.',
            'blank': 'Enter a model.'
        }
    )
    year = models.CharField(max_length=4,
        error_messages = {
            'invalid': 'Year must have 4 characters.',
            'blank': 'Enter a year.'
        }
    )
    seats = models.CharField(max_length=10, 
        error_messages = {
            'invalid': 'Seats must not have more than 10 characters.',
            'blank': 'Enter the number of seats.'
        }
    )
    bedLength = models.CharField(max_length=10,
        error_messages = {
            'invalid': 'Bed length must not have more than 10 characters.',
            'blank': 'Enter the bed length.'
        }
    )
    color = models.CharField(max_length=10,
        error_messages = {
            'invalid': 'Color must not have more than 10 characters.',
            'blank': 'Enter the color.'
        }
    )
    VIN = models.CharField(max_length=17, unique=True,
        error_messages = {
            'invalid': 'Enter a valid VIN.',
            'blank': 'Enter the VIN.'
        },
        validators = [
            RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='VIN must be alphanumeric.',
                code='invalid_VIN')
        ]
    )
    currentMileage = models.CharField(max_length=7,
        error_messages = {
            'invalid': 'Current milieage must not have more than 7 characters.',
            'blank': 'Enter the current mileage.'
        }
    )
    serviceInterval = models.CharField(max_length=50,
        error_messages = {
            'invalid': 'Service internal must not have more than 50 characters.',
            'blank': 'Enter the service interval.'
        }
    )
    nextService = models.CharField(max_length=50,
        error_messages = {
            'invalid': 'Service internal must not have more than 50 characters.',
            'blank': 'Enter the service interval.'
        }
    )

    def  __str__(self):
        return self.make