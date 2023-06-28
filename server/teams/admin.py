from django.contrib import admin

from .models import Team, User

##!! Horizontal filtering not working
class UserAdmin(admin.ModelAdmin):
    team_horizontal = ("team_id")

# Register your models here.
admin.site.register(User)
admin.site.register(Team)
