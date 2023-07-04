from django.db import models
from api.team.models import Team


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=200)
    is_public = models.BooleanField()
    is_archived = models.BooleanField()
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
