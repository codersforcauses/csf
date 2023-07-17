from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Event, Team
from api.users.models import User

import datetime


class EventTests(APITestCase):
    def setUp(self):
        createTeam = Team.objects.create(
                name="mockTeam",
                join_code="mockTeam",
        )
        Event.objects.create(
            name="eventTestPublic",
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            description="public event for unit test",
            is_public=True,
            is_archived=False,
        )
        Event.objects.create(
            name="eventTestPrivate",
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            description="private event for unit test",
            is_public=False,
            is_archived=True,
            team_id=createTeam,
        )


    def test_create_event(self):
        created_event_name = "createEventTestPublic"
        created_event_description = "public event for unit test"
        response = self.client.post(
            reverse("event:create-event"),
            {
                "name": created_event_name,
                "start_date": datetime.date.today(),
                "end_date": datetime.date.today(),
                "description": created_event_description,
                "is_public": True,
                "is_archived": False,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



    def test_get_events(self):
        response = self.client.get(reverse("event:get-events"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_count = 0
        for _ in response.data:
            data_count = data_count + 1
        self.assertEqual(1, data_count) # We only want to return the public events

    def test_update_private_event(self):
        eventBeforeUpdate = Event.objects.get(name="eventTestPrivate")
        response = self.client.put(
            reverse(
                "event:update-event",
                kwargs={"event_id": eventBeforeUpdate.event_id}
                ),
            {
                "name": "updateEventTestPrivate",
                "start_date": datetime.date.today(),
                "end_date": datetime.date.today(),
                "description": "unit test try update",
                "is_public": True,
                "is_archived": False,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_public_event(self):
        eventBeforeUpdate = Event.objects.get(name="eventTestPublic")
        response = self.client.put(
            reverse(
                "event:update-event",
                kwargs={"event_id": eventBeforeUpdate.event_id}
                ),
            {
                "name": "updateEventTestPrivate",
                "start_date": datetime.date.today(),
                "end_date": datetime.date.today(),
                "description": "unit test try update",
                "is_public": True,
                "is_archived": False,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, "User not authenticated")

    def test_delete_private_event(self):
        eventToDelete = Event.objects.get(name="eventTestPrivate")
        response = self.client.delete(
            reverse(
                "event:delete-event",
                kwargs={"event_id": eventToDelete.event_id}
                ),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_public_event(self):
        eventToDelete = Event.objects.get(name="eventTestPublic")
        response = self.client.delete(
            reverse(
                "event:delete-event",
                kwargs={"event_id": eventToDelete.event_id}
                ),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, "User not authenticated")
