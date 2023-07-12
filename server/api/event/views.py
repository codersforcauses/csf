from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse

from .models import Event
from .serializers import EventSerialiser


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
    if request.user.is_authenticated:
        if (request.user.team_id is not None):
            events = Event.objects.filter(team_id=request.user.team_id)
            team_serializer = EventSerialiser(events, many=True)
            return Response(team_serializer.data)
        else:
            events = Event.objects.all()
            serializer = EventSerialiser(events, many=True)
            return HttpResponse(serializer.data)
    else:
        events = Event.objects.filter(is_public=True)
        limited_serializer = EventSerialiser(events, many=True)
        return Response(limited_serializer.data)


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
