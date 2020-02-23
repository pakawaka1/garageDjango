from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=[20, 'Make must not have more than 20 characters.'])
    model = models.CharField(max_length=[20, 'Model must not have more than 20 characters.'])
    year = models.CharField(min_length=[4 'Year must have at least 4 characters.'], max_length=[4, 'Year must not have more than 4 characters.'])
    seats = models.CharField(max_length=[10, 'Seats must not have more than 10 characters.'])
    color = models.CharField(max_length=[10, 'Width must not have more than 10 characters.'])
    VIN = models.CharField(min_length=[17, 'VIN must not have less than 17 characters.'], max_length=[17, 'VIN must not have more than 17 characters.'])
    currentMileage = models.CharField(max_length=[7, 'Current mileage must not have more than 7 characters.'])
    serviceInterval = models.CharField(max_length=50)
    nextService = models.CharField(max_length=50)

    def  __str__(self):
        return self.name