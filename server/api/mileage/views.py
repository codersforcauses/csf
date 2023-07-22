from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Mileage
from ..users.models import User
from ..team.models import Team
from .serializers import MileageSerializer, UserSerializer, UserLeaderboardSerializer, TeamLeaderboardSerializer  # , PostMileageSerializer
from django.core.exceptions import ObjectDoesNotExist
import copy

import datetime

CHALLENGE_LENGTH = 14  # days
LEADERBOARD_SIZE = 100


@api_view(['GET'])
def get_mileage(request, user):
    if request.user.is_authenticated is False:
        return Response("User not authenticated", status=401)
    else:
        mileages = Mileage.objects.filter(user=user)
        # only get mileages within current challenge period
        if 'challenge' in request.GET:
            user = User.objects.get(id=user)
            if user.challenge_start_date is None:
                mileages = []
            # end challenge period if days are up
            elif (datetime.date.today() - user.challenge_start_date).days > CHALLENGE_LENGTH:
                user_serializer = UserSerializer(instance=user, data={'challenge_start_date': None})
                if user_serializer.is_valid():
                    user_serializer.save()
                mileages = []
            else:
                mileages = filter(
                    lambda m: user.challenge_start_date and m.date >= user.challenge_start_date,
                    mileages
                )
        serializer = MileageSerializer(mileages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_mileage(request):
    if request.user.is_authenticated is False:
        return Response("User not authenticated", status=401)
    else:
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response(user.first_name, status=status.HTTP_400_BAD_REQUEST)
        # start challenge for User if not already started
        challenge_start_date = user.challenge_start_date or datetime.date.today()
        # reset challenge if time is up
        if (datetime.date.today() - challenge_start_date).days > CHALLENGE_LENGTH:
            challenge_start_date = datetime.date.today()
        user_data = {
            'id': user.id,
            'challenge_start_date': challenge_start_date
        }
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
        result = {"leaderboard": calculate_leaderboard_ranks(leaderboard_serializer.data[:LEADERBOARD_SIZE])}
        if "username" in request.GET:
            rank, user_mileage, index = get_rank_and_mileage_from_leaderboard(leaderboard_serializer.data, request.GET["username"], "username")
            if rank != -1 and user_mileage != -1:
                result["user"] = {"username": request.GET["username"], "rank": rank, "total_mileage": user_mileage}
    else:
        leaderboard_serializer = TeamLeaderboardSerializer(Team.objects.order_by("-total_mileage"), many=True)
        result = {"leaderboard": calculate_leaderboard_ranks(leaderboard_serializer.data[:LEADERBOARD_SIZE])}
        if "team_name" in request.GET:
            print(leaderboard_serializer.data)
            rank, team_mileage, index = get_rank_and_mileage_from_leaderboard(leaderboard_serializer.data, request.GET["team_name"], "name")
            if rank != -1 and team_mileage != -1:
                print(rank)
                result["team"] = {"name": request.GET["team_name"], "bio": leaderboard_serializer.data[index]["bio"],
                                  "rank": rank, "total_mileage": team_mileage}

    return Response(result)


def get_rank_and_mileage_from_leaderboard(leaderboard, username, field_name):
    i = 0
    length = len(leaderboard)
    rank = -1
    mileage = -1
    index = -1
    # We step through the leaderboard until we find a user/team with the matching name
    # Once we achieve that, we step back through the leaderboard to make sure the previous
    # user/team has a bigger mileage, since that means they should have different ranks
    while i >= 0 and i < length:
        if mileage == -1 and leaderboard[i][field_name] == username:
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
def calculate_leaderboard_ranks(leaderboard):
    ranked_leaderboard = []
    for i in range(len(leaderboard)):
        if i > 0 and leaderboard[i]["total_mileage"] == leaderboard[i-1]["total_mileage"]:
            ranked_entry = leaderboard[i]
            ranked_entry["rank"] = ranked_leaderboard[i-1]["rank"]
            ranked_leaderboard.append(ranked_entry)
        else:
            ranked_entry = leaderboard[i]
            ranked_entry["rank"] = i+1
            ranked_leaderboard.append(ranked_entry)
    return ranked_leaderboard
