from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SubTeam
from .serializers import SubTeamSerialiser
from ..users.models import User
from ..users.serializers import UserSerialiser

from django.db.models import Q


@api_view(['POST'])
def create_subteam(request):
    serialiser = SubTeamSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data)


@api_view(['GET'])
def get_subteams(request, team_id):
    subteams = SubTeam.objects.filter(team_id=team_id)
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


@api_view(['GET'])
def get_subteam_users(request, subteam_id):
    if request.user.is_authenticated is False:
        return Response("User not authenticated", status=403)
    else:
        users = User.objects.filter(Q(subteam_id=subteam_id) & Q(team_id=request.user.team_id))
        serialiser = UserSerialiser(users, many=True)
        return Response(serialiser.data, status=200)
