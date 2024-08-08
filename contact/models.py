from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    subject = models.CharField(max_length=25)
    message = models.TextField()

    def __str__(self):
        return self.name

    