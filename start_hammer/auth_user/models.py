from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
import random

class Enter(models.Model):
    
    inv_code=models.CharField(max_length=6, default=None)
    phone_number = PhoneNumberField(unique = True, null = True, blank = False) # Here

class Code (models.Model):
    code =models.CharField(max_length=4, default=None)
class Profile(models.Model):
    inv_code_fr=models.CharField(max_length=6, default=None)

# Create your models here.
