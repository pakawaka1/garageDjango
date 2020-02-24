from django.db import models
from django.core.validators import EmailValidator

class Auth(models.Model):
    name = models.CharField(max_length=10,
        error_messages = {
            'invalid': 'Name must not have more than 20 characters.',
            'blank': 'Enter a name.'
        }
    )
    email = models.CharField(max_length=30, unique=True, 
        error_messages = {
            'invalid': 'Enter a valid email address.',
            'blank': 'Enter an email address'
        }, 
        validators = [
            EmailValidator(
                message='Email must be valid.',
                code='invalid_email'
            )
        ]
    )
    password = models.CharField(max_length=30,
        error_messages = {
            'blank': 'Enter a password'
        }
    )

    def  __str__(self):
        return self.name