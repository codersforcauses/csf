from django.contrib import admin
from .models import Team
# Register your models here.


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'name')


admin.site.register(Team, TeamAdmin)
