from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomModel(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
