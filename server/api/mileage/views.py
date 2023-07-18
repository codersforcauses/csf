from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Mileage
from ..users.models import User
from .serializers import MileageSerializer, UserSerializer, LeaderboardSerializer  # , PostMileageSerializer

import datetime

CHALLENGE_LENGTH = 14  # days


@api_view(['GET'])
def get_mileage(request, user):
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
    return Response(serializer.data)


@api_view(['POST'])
def post_mileage(request):
    try:
        user = User.objects.get(id=request.data['user'])
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_leaderboard(request):
    if request.GET["type"] == "users":
        leaderboard_serializer = LeaderboardSerializer(User.objects.order_by("-total_mileage"), many=True)
        return Response(leaderboard_serializer.data)
    else:
        # TODO
        return Response()
