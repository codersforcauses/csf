from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("change_password/<int:id>", views.change_password, name="change-password"),
    path("request_reset_password/", views.request_reset_password, name="request-reset-password")
]
