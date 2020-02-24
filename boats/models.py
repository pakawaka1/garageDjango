from django.db import models
from django.core.validators import RegexValidator

class Boat(models.Model):
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
    length = models.CharField(max_length=20, 
        error_messages = {
            'invalid': 'Length must not have more than 20 characters.',
            'blank': 'Enter the length.'
        }
    )
    width = models.CharField(max_length=20,
        error_messages = {
            'invalid': 'Width must not have more than 20 characters.',
            'blank': 'Enter the width.'
        }
    )
    HIN = models.CharField(max_length=13, unique=True,
        error_messages = {
            'invalid': 'Enter a valid HIN.',
            'blank': 'Enter a HIN.'
        },
        validators = [ 
            RegexValidator( 
                regex='^[a-zA-Z0-9]*$',
                message='HIN must be alphanumeric.',
                code='invalid_HIN'
            )         
        ]
    )
    currentHours = models.CharField(max_length=7,
        error_messages = {
            'invalid': 'Current hours must not have more than 7 characters.',
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