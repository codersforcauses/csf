from django.urls import path
from . import views

app_name = "subteam"
urlpatterns = [
    path("create_subteam/", views.create_subteam, name="create-subteam"),
    path("get_subteams/", views.get_subteams, name="get-subteams"),
    path("get_subteam/<int:subteam_id>", views.get_subteam, name="get-subteam"),
    path("update_subteam/<int:subteam_id>", views.update_subteam, name="update-subteam"),
    path("delete_subteam/<int:subteam_id>", views.delete_subteam, name="delete-subteam"),
]
