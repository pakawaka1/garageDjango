from django.db import models

class Boat(models.Model):
    make = models.CharField(max_length=[20, 'Make must not have more than 20 characters.'])
    model = models.CharField(max_length=[20, 'Model must not have more than 20 characters.'])
    year = models.CharField(min_length=[4 'Year must have at least 4 characters.'], max_length=[4, 'Year must not have more than 4 characters.'])
    length = models.CharField(max_length=[20, 'Length must not have more than 20 characters.'])
    width = models.CharField(max_length=[20, 'Width must not have more than 20 characters.'])
    HIN = models.CharField(min_length=[12, 'HIN must have at least 12 characters.'], max_length=[13, 'HIN must not have more than 13 characters.'])
    currentHours = models.CharField(max_length=[7, 'Current hours must not have more than 7 characters.'])
    serviceInterval = models.CharField(max_length=50)
    nextService = models.CharField(max_length=50)

    def  __str__(self):
        return self.name