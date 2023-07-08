from django.urls import path
from . import views

app_name = "team"
urlpatterns = [
    path("team/", views.create_team, name="create-team"),
    path("team/", views.get_teams, name="get-teams"),
    path("team/<int:team_id>", views.get_team, name="get-team"),
    path("team/<int:team_id>", views.update_team, name="update-team"),
    path("team/<int:team_id>", views.delete_team, name="delete-team"),
]
