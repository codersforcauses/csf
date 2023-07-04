from django.db import models
import datetime


class Mileage(models.Model):
    mileage_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    # user = models.ForeignKey("User")
    kilometres = models.IntegerField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.user_id} {self.kilometres} {self.date}'