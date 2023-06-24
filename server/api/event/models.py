from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    is_public = models.BooleanField()
    is_archived = models.BooleanField()
    # team_id =

    