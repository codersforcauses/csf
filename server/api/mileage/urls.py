from django.urls import path
from . import views

app_name = "mileage"
urlpatterns = [
    path("get_leaderboard/", views.get_leaderboard, name="get-leaderboard"),
    path("get_mileage", views.get_mileage, name="get-mileage"),
    path("post_mileage", views.post_mileage, name="post-mileage"),
]
