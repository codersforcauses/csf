from django.urls import path

from . import views

app_name = "event"
urlpatterns = [
    path("create/", views.create_event, name="create-event"),
    path("get/<int:event_id>", views.get_event, name="get-event"),
    path("update/<int:event_id>", views.update_event, name="update-event"),
    path("delete/<int:event_id>", views.delete_event, name="delete-event"),
]
