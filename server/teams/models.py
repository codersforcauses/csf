from django.db import models
import hashlib

# Create your models here.
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True)
    join_code = models.CharField(unique=True, default=None)

    def __str__(self):
        return f"{self.name} - {self.join_code}"
    
    def save(self, *args, **kwargs):
        if self.join_code is None:
            self.join_code = hashlib.sha256(self.name.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)  # Call the "real" save() method.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True)
    first_name = models.CharField(max_length = 25)    
    last_name = models.CharField(max_length = 25)    
    email = models.EmailField(max_length = 254, unique=True)
    team_id = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='memberOf')
    is_admin = models.BooleanField()

    def __str__(self):
        return f"{self.username}"
    