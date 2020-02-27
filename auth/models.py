from django.db import models
from django.core.validators import EmailValidator


class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=30, unique=True,
                              error_messages={
                                  'unique': "This email address has already been registered."}
                              )
    password = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
