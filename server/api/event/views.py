from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import admin
from django.http import HttpResponse

from .models import Event
from .serializers import EventSerialiser
import csv


@api_view(['POST'])
def create_event(request):
    serialiser = EventSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data, status=200)
    else:
        # print(serialiser)
        return Response(serialiser.errors, status=400)


@api_view(['GET'])
def get_event(request, event_id):
    event = Event.objects.get(event_id=event_id)
    serializer = EventSerialiser(event)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerialiser(events, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_event(request, event_id):
    event = Event.objects.get(event_id=event_id)
    print(event)
    if event.is_public is False:
        serializer = EventSerialiser(instance=event, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    else:
        return Response("Event is not private")


@api_view(['DELETE'])
def delete_event(request, event_id):
    event = Event.objects.get(event_id=event_id)
    if event.is_public is False:
        event.delete()
        return Response("Event successfully deleted")
    else:
        return Response("Event is not private")


def export_eventcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=events.csv'

    events_writer = csv.writer(response)

    events = Event.objects.all()

    events_writer.writerow(['ID', 'Name', 'Start date', 'End date', 'Description', 'Public', 'Archived', 'Team ID'])

    for event in events:
        events_writer.writerow([event.event_id, event.name, event.start_date, event.end_date, event.description, event.is_public, event.is_archived, event.team_id])

    return response


