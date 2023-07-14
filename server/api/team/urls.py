from django.urls import path
from . import views

app_name = "team"
urlpatterns = [
    path("", views.create_team, name="create-team"),
    path("", views.get_teams, name="get-teams"),
    path("<int:team_id>", views.get_team, name="get-team"),
    path("", views.update_team, name="update-team"),
    path("<int:team_id>", views.delete_team, name="delete-team"),
]
