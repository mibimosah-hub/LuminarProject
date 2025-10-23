from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True)