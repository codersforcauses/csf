from django.urls import path
from . import views

# URLConf
app_name = 'teams'
urlpatterns = [
    path('team/', views.team, name="team"),
    path('create_team/', views.create_team, name="create_team"),
    path('join_team/', views.join_team, name="join_team"),
    path('<int:team_id>/edit_team', views.edit_team, name="edit_team"),
    path('<int:team_id>/delete_team', views.delete_team, name="delete_team"),
    path('<int:team_id>/leave_team', views.leave_team, name="leave_team")
]