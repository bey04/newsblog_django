from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomerUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)