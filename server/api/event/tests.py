from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Event, Team

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
            team_id=createTeam,
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        created_event = Event.objects.get(name="createEventTestPublic")
        self.assertEqual(created_event.name, created_event_name)
        self.assertEqual(created_event.start_date, datetime.date.today())
        self.assertEqual(created_event.end_date, datetime.date.today())
        self.assertEqual(created_event.description, created_event_description)
        self.assertTrue(created_event.is_public)
        self.assertFalse(created_event.is_archived)

    def test_get_event(self):
        existingTeam = Team.objects.get()
        one_event = Event.objects.get(name="eventTestPublic")
        response = self.client.get(
            reverse("event:get-event", kwargs={"event_id": one_event.event_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(one_event.name, "eventTestPublic")
        self.assertEqual(one_event.start_date, datetime.date.today())
        self.assertEqual(one_event.end_date, datetime.date.today())
        self.assertEqual(one_event.description, "public event for unit test")
        self.assertTrue(one_event.is_public)
        self.assertFalse(one_event.is_archived)
        self.assertEqual(one_event.team_id, existingTeam)

    def test_get_events(self):
        all_event = Event.objects.all()
        response = self.client.get(reverse("event:get-events"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_count = 0
        for x in response.data:
            data_count = data_count + 1
        self.assertEqual(all_event.count(), data_count)

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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.keys()), 0) # no errors
        self.assertEqual(Event.objects.get(event_id=eventBeforeUpdate.event_id).name, "updateEventTestPrivate")
        self.assertEqual(Event.objects.get(event_id=eventBeforeUpdate.event_id).description, "unit test try update")

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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "Event is not private")

    def test_delete_private_event(self):
        eventCountBeforeDelete = Event.objects.all().count()
        eventToDelete = Event.objects.get(name="eventTestPrivate")
        response = self.client.delete(
            reverse(
                "event:delete-event",
                kwargs={"event_id": eventToDelete.event_id}
                ),
        )
        eventCountAfterDelete = Event.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(eventCountBeforeDelete - 1, eventCountAfterDelete)

    def test_delete_public_event(self):
        eventToDelete = Event.objects.get(name="eventTestPublic")
        response = self.client.delete(
            reverse(
                "event:delete-event",
                kwargs={"event_id": eventToDelete.event_id}
                ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "Event is not private")
