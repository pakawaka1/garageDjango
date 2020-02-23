from django.db import models

class User(models.Model):
    name = models.CharField(max_length=[20 'Name must not have more than 20 characters.'])
    email = models.CharField(max_length=[30 'Email address must not have more than 30 characters.'], unique=true, validators = [EmailValidator(message='Please enter a valid email address.')])
    password = models.CharField(min_length=[7, 'Password must not have less than 7 characters.'], select=true)
     )

    def  __str__(self):
        return self.name