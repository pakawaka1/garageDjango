from django.db import models
from django.core.validators import RegexValidator

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.CharField(max_length=4,
        validators = [ 
            RegexValidator( 
                regex='^[0-9]{4}$',
                message='Year must be a 4-digit number.',
                code='invalid_year'
            )         
        ]
    )
    seats = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    VIN = models.CharField(max_length=17, unique=True,
        error_messages = {
            'unique': "This VIN has already been registered."
        },
        validators = [ 
            RegexValidator( 
                regex='^[a-zA-Z0-9]{17}$',
                message='Invalid VIN.  Please check your VIN.',
                code='invalid_VIN'
            )         
        ]
    )
    currentMileage = models.CharField(max_length=7)
    serviceInterval = models.CharField(max_length=50)
    nextService = models.CharField(max_length=50)

    def  __str__(self):
        return self.make