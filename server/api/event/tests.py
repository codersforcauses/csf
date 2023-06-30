from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Event
from .serializers import EventSerialiser

class EventTests(APITestCase):
    def setUp(self):
        Event.objects.create(event_id=1, name="eventTestPublic", 
                                         description="public event for unit test",
                                         is_public=True, is_archived=False)
        Event.objects.create(event_id=2, name="eventTestArchived", 
                                         description="archived event for unit test",
                                         is_public=True, is_archived=True)
        
    def test_create_event(self):
        response = self.client.post(
            reverse("event:create-event"),
            {   "name":"eventTestPublic", 
                "description":"public event for unit test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_event(self):
        all_event = Event.objects.get()
        response = self.client.get(
            reverse("event:get-event"),
            # {   "name":"eventTestPublic", 
            #     "description":"public event for unit test",
            # },
            # format="json",
        )
        
    def test_get_events(self):
        all_event = Event.objects.get()
        response = self.client.get(
            reverse("event:get-event"),
            # {   "name":"eventTestPublic", 
            #     "description":"public event for unit test",
            # },
            # format="json",
        )

    def test_update_event(self):
        all_event = Event.objects.get()
        response = self.client.get(
            reverse("event:get-event"),
            # {   "name":"eventTestPublic", 
            #     "description":"public event for unit test",
            # },
            # format="json",
        )

    def test_delete_event(self):
        all_event = Event.objects.get()
        response = self.client.get(
            reverse("event:get-event"),
            # {   "name":"eventTestPublic", 
            #     "description":"public event for unit test",
            # },
            # format="json",
        )

