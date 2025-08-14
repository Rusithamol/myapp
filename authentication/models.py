from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Pincode=models.IntegerField(default=0)
    Father_Name=models.CharField(max_length=200)

