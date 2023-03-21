from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField(null=True, default=0)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)