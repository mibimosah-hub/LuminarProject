from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import random
class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True)
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=10,null=True)
    # for creating otp for user
    def generate_otp(self):
        otp=str(random.randint(1000,9999))+str(self.id)
        self.otp=otp #otp table name
        self.save()