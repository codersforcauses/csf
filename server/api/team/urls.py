from django.urls import path
from . import views

app_name = "team"
urlpatterns = [
    path("create/", views.create_team, name="create-team"),
    path("get_teams/", views.get_teams, name="get-teams"),
    path("get/<int:team_id>/", views.get_team, name="get-team"),
    path("edit/<int:team_id>/", views.update_team, name="update-team"),
    path("delete/<int:team_id>/", views.delete_team, name="delete-team"),
]
