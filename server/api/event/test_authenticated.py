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
        self.testuser = User.objects.create_user(username='John', password='John123!', team_id=createTeam, team_admin=True)
        self.testuser.save()

    def get_token(self):
        get_token_url = reverse('auth:jwt_token')
        get_token_body = {
            'username': 'John',
            'password': 'John123!'
        }
        get_token_response = self.client.post(get_token_url, get_token_body, format='json')

        token = get_token_response.data['access']
        return token

    def test_create_event(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
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

    def test_get_events(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        all_event = Event.objects.filter(is_archived=False)
        response = self.client.get(reverse("event:get-events"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_count = 0
        for x in response.data:
            data_count = data_count + 1
        self.assertEqual(all_event.count(), data_count)

    def test_update_private_event(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
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
                "is_public": False,
                "is_archived": False,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "updateEventTestPrivate")
        self.assertEqual(response.data['description'], "unit test try update")

    def test_update_public_event(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
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
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, "User is not authorised to update this event")

    def test_delete_private_event(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
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
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        eventToDelete = Event.objects.get(name="eventTestPublic")
        response = self.client.delete(
            reverse(
                "event:delete-event",
                kwargs={"event_id": eventToDelete.event_id}
                ),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, "User is not authorised to update this event")
