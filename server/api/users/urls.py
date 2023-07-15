from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("change_password/<int:id>", views.change_password, name="change-password"),
    path("request_reset_password/", views.request_reset_password, name="request-reset-password"),
    path("verify_token/", views.verify_token, name="verify-token"),
    path("reset_password/", views.reset_password, name="reset-password"),
    path("<str:username>/", views.get_user, name="get-user"),
    path("join/<int:id>/", views.join_team, name="join-team")
]
