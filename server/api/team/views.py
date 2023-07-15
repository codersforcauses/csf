from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Team
from .serializers import TeamSerialiser


@api_view(['POST'])
def create_team(request):
    if (request.user.is_authenticated is False):
        return Response("User not authenticated", status=401)
    else:
        serialiser = TeamSerialiser(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        else:
            return Response(serialiser.errors, status=400)


@api_view(['GET'])
def get_team(request, team_id):
    team = Team.objects.get(team_id=team_id)
    serializer = TeamSerialiser(team)
    return Response(serializer.data)


@api_view(['GET'])
def get_teams(request):
    teams = Team.objects.all()
    serializer = TeamSerialiser(teams, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_team(request, team_id):
    if (request.user.is_authenticated is False):
        return Response("User is not authenticated", status=401)
    else:
        if (request.user.team_id != team_id and request.user.team_admin is False):
            return Response("User is not authorised to edit this team", status=403)
        else:
            team = Team.objects.get(team_id=team_id)
            serializer = TeamSerialiser(instance=team, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_team(request, team_id):
    if (request.user.is_authenticated is False):
        return Response("User is not authenticated", status=401)
    else:
        if (request.user.team_id != team_id and request.user.team_admin is False):
            return Response("User is not authorised to delete this team", status=403)
        else:
            team = Team.objects.get(team_id=team_id)
            team.delete()
            return Response("Team successfully deleted")
