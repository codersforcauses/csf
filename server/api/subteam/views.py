from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SubTeam
from .serializers import SubTeamSerialiser


@api_view(['POST'])
def create_subteam(request):
    serialiser = SubTeamSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data)


@api_view(['GET'])
def get_subteam(request, subteam_id):
    subteam = SubTeam.objects.get(subteam_id=subteam_id)
    serializer = SubTeamSerialiser(subteam)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def get_subteams(request):
    subteams = SubTeam.objects.all()
    serializer = SubTeamSerialiser(subteams, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_subteam(request, subteam_id):
    subteam = SubTeam.objects.get(subteam_id=subteam_id)
    serializer = SubTeamSerialiser(instance=subteam, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def delete_subteam(request, subteam_id):
    subteam = SubTeam.objects.get(subteam_id=subteam_id)
    subteam.delete()
    return Response("SubTeeam successfully deleted")
