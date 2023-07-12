from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from server.common.utils import model_data_2_csv

from .models import Event
from .serializers import EventSerialiser


@api_view(["POST"])
def create_event(request):
    serialiser = EventSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data, status=200)
    else:
        # print(serialiser)
        return Response(serialiser.errors, status=400)


@api_view(["GET"])
def get_event(request, event_id):
    event = Event.objects.get(event_id=event_id)
    serializer = EventSerialiser(event)
    print(serializer.data)
    return Response(serializer.data)


@api_view(["GET"])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerialiser(events, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
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


@api_view(["DELETE"])
def delete_event(request, event_id):
    event = Event.objects.get(event_id=event_id)
    if event.is_public is False:
        event.delete()
        return Response("Event successfully deleted")
    else:
        return Response("Event is not private")


def export_events_csv(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="events.csv"'},
    )

    model_data_2_csv("Event", response)

    return response
