from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Event

import datetime

class EventTests(APITestCase):
    def setUp(self):
        Event.objects.create( 
                                name="eventTestPublic", 
                                start_date = datetime.date.today(),
                                end_date = datetime.date.today(),
                                description="public event for unit test",
                                is_public=True, 
                                is_archived=False)
        Event.objects.create(
                                name="eventTestPrivate", 
                                start_date = datetime.date.today(),
                                end_date = datetime.date.today(),
                                description="private event for unit test",
                                is_public=False, 
                                is_archived=True)
        
    def test_create_event(self):
        response = self.client.post(
            reverse("event:create-event"),
            {   
                "name":"createEventTestPublic", 
                "start_date":datetime.date.today(),
                "end_date":datetime.date.today(),
                "description":"public event for unit test",
                "is_public":True,
                "is_archived":False
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        created_event = Event.objects.get(name="createEventTestPublic")
        self.assertEqual(created_event.name, "createEventTestPublic")
        self.assertEqual(created_event.start_date, datetime.date.today())
        self.assertEqual(created_event.end_date, datetime.date.today())
        self.assertEqual(created_event.description, "public event for unit test")
        self.assertEqual(created_event.is_public, True)
        self.assertEqual(created_event.is_archived, False)        
    
    def test_get_event(self):
        one_event = Event.objects.get(name="eventTestPublic")
        response = self.client.get(
            reverse("event:get-event", kwargs={"event_id":one_event.event_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(one_event.name, "eventTestPublic")
        self.assertEqual(one_event.start_date, datetime.date.today())
        self.assertEqual(one_event.end_date, datetime.date.today())
        self.assertEqual(one_event.description, "public event for unit test")
        self.assertEqual(one_event.is_public, True)
        self.assertEqual(one_event.is_archived, False)  
        
    def test_get_events(self):
        all_event = Event.objects.all()
        response = self.client.get(
            reverse("event:get-events")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_count = 0
        for x in response.data:
            data_count = data_count + 1
        self.assertEqual(all_event.count(), data_count)

    def  test_update_private_event(self):
        eventBeforeUpdate = Event.objects.get(name="eventTestPrivate")
        response = self.client.put(
            reverse("event:update-event",kwargs={"event_id":eventBeforeUpdate.event_id}),
            {   
                "name":"updateEventTestPrivate", 
                "description":"unit test try update",
            },
            format="json",
            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "updateEventTestPrivate")
        self.assertEqual(response.data["description"], "unit test try update")

    def  test_update_public_event(self):
        eventBeforeUpdate = Event.objects.get(name="eventTestPublic")
        response = self.client.put(
            reverse("event:update-event",kwargs={"event_id":eventBeforeUpdate.event_id}),
            {   
                "name":"updateEventTestPrivate", 
                "description":"unit test try update",
            },
            format="json",
            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "Event is not private")

    def test_delete_private_event(self):
        eventCountBeforeDelete = Event.objects.all().count()
        eventToDelete = Event.objects.get(name="eventTestPrivate")
        response = self.client.delete(
            reverse("event:delete-event",kwargs={"event_id":eventToDelete.event_id}),
        )
        eventCountAfterDelete = Event.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(eventCountBeforeDelete - 1, eventCountAfterDelete)

    def test_delete_public_event(self):
        eventCountBeforeDelete = Event.objects.all().count()
        eventToDelete = Event.objects.get(name="eventTestPublic")
        response = self.client.delete(
            reverse("event:delete-event",kwargs={"event_id":eventToDelete.event_id}),
        )
        eventCountAfterDelete = Event.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "Event is not private")
