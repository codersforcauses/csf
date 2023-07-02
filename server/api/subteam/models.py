from django.db import models


class SubTeam(models.Model):
    subteam_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    # to add in later like chantelle said in issue
    # team_id = models.ForeignKey()

    def __str__(self):
        return f"{self.name}"
