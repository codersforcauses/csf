from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Mileage
from ..users.models import User
from ..team.models import Team
from .serializers import MileageSerializer, UserSerializer, UserLeaderboardSerializer, TeamLeaderboardSerializer  # , PostMileageSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Sum, Q


import datetime

CHALLENGE_LENGTH = datetime.timedelta(days=14)
LEADERBOARD_SIZE = 100

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_mileage(request: HttpRequest):
    queries = []
    if "user" in request.GET:
        queries.append(Q(user__in=request.GET.getlist("user")))
    if "team" in request.GET:
        queries.append(Q(user__team_id__in=request.GET.getlist("team")))
    if request.GET.get("challenge"):
        # only get mileages within *current* challenge period
        queries.append(
            Q(
                user__challenge_start_date__gte=datetime.date.today() - CHALLENGE_LENGTH,
                date__range=(
                    F("user__challenge_start_date"),
                    F("user__challenge_start_date") + CHALLENGE_LENGTH,
                ),
            )
        )

    mileage = Mileage.objects.filter(*queries)
    return Response(
        mileage.aggregate(Sum("kilometres"))["kilometres__sum"] if request.GET.get("sum")
        else MileageSerializer(mileage, many=True).data
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_mileage(request):
    try:
        user = User.objects.get(id=request.user.id)
    except ObjectDoesNotExist:
        return Response(request.user.first_name, status=status.HTTP_400_BAD_REQUEST)
    # start challenge for User if not already started
    challenge_start_date = user.challenge_start_date or datetime.date.today()
    # reset challenge if time is up
    if (datetime.date.today() - challenge_start_date) > CHALLENGE_LENGTH:
        challenge_start_date = datetime.date.today()
    user_data = {"id": user.id, "challenge_start_date": challenge_start_date}
    user_serializer = UserSerializer(instance=user, data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        serializer = MileageSerializer(data=request.data)
        if serializer.is_valid():
            mileage = serializer.save()
            response_data = MileageSerializer(mileage).data
            return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_leaderboard(request):
    if request.GET["type"] == "users":
        leaderboard_serializer = UserLeaderboardSerializer(User.objects.filter(is_staff=False).order_by("-total_mileage"), many=True)
        result = {"leaderboard": calculate_leaderboard_ranks(leaderboard_serializer.data[:LEADERBOARD_SIZE], "id")}
        if "user_id" in request.GET:
            rank, user_mileage, index = get_rank_and_mileage_from_leaderboard(leaderboard_serializer.data, int(request.GET["user_id"]), "id")
            if rank != -1 and user_mileage != -1:
                result["user"] = {"username": leaderboard_serializer.data[index]["username"], "rank": rank, "total_mileage": user_mileage}
    else:
        leaderboard_serializer = TeamLeaderboardSerializer(Team.objects.order_by("-total_mileage"), many=True)
        result = {"leaderboard": calculate_leaderboard_ranks(leaderboard_serializer.data[:LEADERBOARD_SIZE], "team_id")}
        if "team_id" in request.GET:
            rank, team_mileage, index = get_rank_and_mileage_from_leaderboard(leaderboard_serializer.data, int(request.GET["team_id"]), "team_id")
            if rank != -1 and team_mileage != -1:
                result["team"] = {"name": leaderboard_serializer.data[index]["name"], "bio": leaderboard_serializer.data[index]["bio"],
                                  "rank": rank, "total_mileage": team_mileage}

    return Response(result)


def get_rank_and_mileage_from_leaderboard(leaderboard, id, field_name):
    i = 0
    length = len(leaderboard)
    rank = -1
    mileage = -1
    index = -1
    # We step through the leaderboard until we find a user/team with the matching name
    # Once we achieve that, we step back through the leaderboard to make sure the previous
    # user/team has a bigger mileage, since that means they should have different ranks
    while i >= 0 and i < length:
        if mileage == -1 and leaderboard[i][field_name] == id:
            index = i
            mileage = leaderboard[i]['total_mileage']
            rank = i + 1
        elif mileage != -1:
            # we step backwards through the leaderboard until we find a user/team with greater
            # mileage, or until we've gone the whole way back
            if leaderboard[i]['total_mileage'] > mileage:
                rank = i + 2
                break
            elif i == 0:
                rank = i + 1
                break
        if mileage == -1:
            i += 1
        else:
            i -= 1
    return rank, mileage, index


# users with the exact same mileage should have the same rank
def calculate_leaderboard_ranks(leaderboard, id_field_name):
    ranked_leaderboard = []
    for i in range(len(leaderboard)):
        # copy because we'll need the id field if we're also calculating the rank of a specific user
        ranked_entry = leaderboard[i].copy()
        # no need to send the id back to the frontend
        ranked_entry.pop(id_field_name)
        if i > 0 and leaderboard[i]["total_mileage"] == leaderboard[i-1]["total_mileage"]:
            ranked_entry["rank"] = ranked_leaderboard[i-1]["rank"]
        else:
            ranked_entry["rank"] = i+1
        ranked_leaderboard.append(ranked_entry)
    return ranked_leaderboard
