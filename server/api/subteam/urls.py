from django.urls import path
from . import views

app_name = "subteam"
urlpatterns = [
    path("create/", views.create_subteam, name="create-subteam"),
    path("get_subteams/<int:team_id>", views.get_subteams, name="get-subteams"),
    path("update_subteam/<int:subteam_id>", views.update_subteam, name="update-subteam"),
    path("delete_subteam/<int:subteam_id>", views.delete_subteam, name="delete-subteam"),
    path("get_users/<int:subteam_id>", views.get_subteams, name="get-subteam-users"),
    path("get_available_users/", views.get_available_users, name="get-available-users"),
    path("edit_user/<int:subteam_id>/<int:user_id>", views.edit_user_to_subteam, name="edit-user"),

]
