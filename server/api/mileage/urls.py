from django.urls import path
from . import views

app_name = "mileage"
urlpatterns = [
    path("get_mileage/user/<int:user>", views.get_mileage_by_user, name="get-mileage-by-user"),
    path("get_mileage/team/<int:team>", views.get_mileage_by_team, name="get-mileage-by-team"),
    path("post_mileage/", views.post_mileage, name="post-mileage"),
]
