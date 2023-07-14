from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Mileage
from ..users.models import User
from .serializers import MileageSerializer, UserSerializer #, PostMileageSerializer

import datetime

CHALLENGE_LENGTH = 14 # days

@api_view(['GET'])
def get_mileage(request, user):
    mileages = Mileage.objects.filter(user=user)
    
    if 'challenge' in request.data:
        user = User.objects.get(id=user)

        if (datetime.date.today() - user.challenge_start_date).days > CHALLENGE_LENGTH:
            # reset challenge
            user_data = {
                'id': request.data['user'],
                'challenge_start_date': user.challenge_start_date or datetime.date.today()
            }
            user_serializer = UserSerializer(instance=user, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()

        # only get mileages within current challenge period
        mileages = filter(lambda m: m.date >= user_serializer.challenge_start_date, mileages)

    serializer = MileageSerializer(mileages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_mileage(request):
    # start challenge for User if not already started
    user = User.objects.get(id=request.data['user'])
    user_data = {
        'id': request.data['user'],
        'challenge_start_date': user.challenge_start_date or datetime.date.today()
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
