from django.urls import path

from . import views 

app_name="event"
urlpatterns = [
    path("create_event/", views.create_event, name="createEvent"),
    path("get_event/<int:event_id>", views.get_event, name="getEvent"),
    path("update_event/<int:event_id>", views.update_event, name="updateEvent"),
    path("delete_event/<int:event_id>", views.delete_event, name="deleteEvent"),
]
