from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SubTeam
from .serializers import SubTeamSerialiser
from ..users.models import User
from ..users.serializers import UserSerialiser, UserUpdateSerializer

from django.db.models import Q


@api_view(['POST'])
def create_subteam(request):
    if (request.user.is_authenticated is False):
        return Response("User not authenticated", status=401)
    else:
        if (request.user.team_admin is False):
            return Response("User is not authorised to create a subteam", status=403)
        else:
            serialiser = SubTeamSerialiser(data=request.data)
            if serialiser.is_valid():
                serialiser.save()
                return Response(serialiser.data, status=200)
            else:
                return Response(serialiser.errors, status=400)


@api_view(['GET'])
def get_subteams(request, team_id):
    subteams = SubTeam.objects.filter(team_id=team_id)
    serializer = SubTeamSerialiser(subteams, many=True)
    return Response(serializer.data, status=200)


@api_view(['PUT'])
def update_subteam(request, subteam_id):
    if (request.user.is_authenticated is False):
        return Response("User not authenticated", status=401)
    else:
        if (request.user.team_admin is False):
            return Response("User is not authorised to update a subteam", status=403)
        else:
            subteam = SubTeam.objects.get(subteam_id=subteam_id)
            serializer = SubTeamSerialiser(instance=subteam, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_subteam(request, subteam_id):
    if (request.user.is_authenticated is False):
        return Response("User not authenticated", status=401)
    else:
        users = User.objects.filter(Q(subteam_id=subteam_id) & Q(team_id=request.user.team_id))
        serialiser = UserUpdateSerializer(users, many=True)
        return Response(serialiser.data, status=200)


@api_view(['GET'])
def get_available_users(request):
    if request.user.is_authenticated is False:
        return Response("User not authenticated", status=403)
    else:
        users = User.objects.filter(Q(subteam_id=None) & Q(team_id=request.user.team_id))
        serialiser = UserSerialiser(users, many=True)
        return Response(serialiser.data, status=200)


@api_view(['PUT'])
def edit_user_to_subteam(request, subteam_id, user_id):
    user = User.objects.get(user_id=user_id)
    user.subteam_id = subteam_id
    user.save()
    return Response("User added to subteam", status=200)
