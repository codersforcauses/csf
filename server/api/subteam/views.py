from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SubTeam
from .serializers import SubTeamSerialiser


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
        if (request.user.team_admin is False):
            return Response("User is not authorised to delete a subteam", status=403)
        else:
            if (request.user.team_id != SubTeam.objects.get(subteam_id=subteam_id).team_id):
                return Response("User is not authorised to delete this subteam", status=403)
            else:
                subteam = SubTeam.objects.get(subteam_id=subteam_id)
                subteam.delete()
                return Response("SubTeeam successfully deleted", status=200)
