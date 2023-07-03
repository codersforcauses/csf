from django.db import models
from api.team.models import Team


class SubTeam(models.Model):
    subteam_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
