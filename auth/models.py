from django.db import models
from django.core.validators import EmailValidator

class Auth(models.Model):

    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=30, unique=True,
        error_messages = {
            'unique': "This email address has already been registered."
        }
    )
    
    # email = models.CharField(max_length=30, unique=True,
    #     validators = [
    #         EmailValidator(
    #             message='Email must be valid.',
    #             code='invalid_email'
    #         )
    #     ]
    # )
    password = models.CharField(max_length=30)

    def  __str__(self):
        return self.name