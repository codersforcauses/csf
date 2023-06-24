from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True) # primary key
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_signup = models.BooleanField() # boolean
    has_consent = models.BooleanField() # boolean


    def __str__(self):
        return self.user_id