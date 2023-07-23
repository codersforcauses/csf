from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Mileage
from ..users.models import User
from .serializers import MileageSerializer, UserSerializer  # , PostMileageSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Sum, Q


import datetime

CHALLENGE_LENGTH = datetime.timedelta(days=14)


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
        return Response(user.first_name, status=status.HTTP_400_BAD_REQUEST)
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
