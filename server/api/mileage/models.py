from django.db import models
import datetime
from ..users.models import User


class Mileage(models.Model):
    mileage_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kilometres = models.FloatField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.user.id} {self.kilometres} {self.date}'
