from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("change_password/", views.change_password, name="change-password"),
]
