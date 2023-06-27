from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=200)
    is_public = models.BooleanField()
    is_archived = models.BooleanField()
    # to add in later like chantelle said in issue
    # team_id =
    def __str__(self):
        return self.name

    