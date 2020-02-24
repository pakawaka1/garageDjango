from django.db import models
from django.core.validators import RegexValidator

class Boat(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.CharField(max_length=4,
        validators = [ 
            RegexValidator( 
                regex='^[a-zA-Z0-9].{4,4}$',
                message='Year must have 4 characters.',
                code='invalid_HIN'
            )         
        ]
    )
    length = models.CharField(max_length=20)
    width = models.CharField(max_length=20)
    HIN = models.CharField(max_length=17, unique=True,
        validators = [ 
            RegexValidator( 
                regex='^[a-zA-Z0-9].{12,13}$',
                message='Invalid HIN.  Please check your HIN.',
                code='invalid_HIN'
            )         
        ]
    )
    currentHours = models.CharField(max_length=7)
    serviceInterval = models.CharField(max_length=50)
    nextService = models.CharField(max_length=50)

    def  __str__(self):
        return self.make