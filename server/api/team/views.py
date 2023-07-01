from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Team
from .serializers import TeamSerialiser


@api_view(['POST'])
def create_team(request):
    serialiser = TeamSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data)


@api_view(['GET'])
def get_team(request, team_id):
    team = Team.objects.get(team_id=team_id)
    serializer = TeamSerialiser(team)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def get_teams(request):
    teams = Team.objects.all()
    serializer = TeamSerialiser(teams, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_team(request, team_id):
    team = Team.objects.get(team_id=team_id)
    if team.is_public is False:
        serializer = TeamSerialiser(instance=team, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("Team is not private")


@api_view(['DELETE'])
def delete_team(request, team_id):
    team = Team.objects.get(team_id=team_id)
    if team.is_public is False:
        team.delete()
        return Response("Team successfully deleted")
    else:
        return Response("Team is not private")
