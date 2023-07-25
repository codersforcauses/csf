from django.db import models
import hashlib


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=254)
    join_code = models.CharField(unique=True, default=None)
    bio = models.TextField(default="")
    total_mileage = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.join_code}"

    def save(self, *args, **kwargs):
        if self.join_code is None:
            # self.join_code = hashlib.sha256(self.name.encode('utf-8')).hexdigest()
            self.join_code = hashlib.shake_256(self.name.encode("utf-8")).hexdigest(length=8)
        super().save(*args, **kwargs)  # Call the "real" save() method.e
