from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Event
from .serializers import EventSerialiser


@api_view(['POST'])
def create_event(request):
    serialiser = EventSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data)


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
    if event.is_public is False:
        serializer = EventSerialiser(instance=event, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
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

