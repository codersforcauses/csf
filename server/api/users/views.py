from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import ChangePasswordSerializer, RequestResetPasswordSerializer, ResetPasswordSerializer, UserSerialiser
# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError

import uuid
import datetime


@api_view(['GET'])
def get_user(request, username):
    user = User.objects.get(username=username)
    serializer = UserSerialiser(user)
    return Response(serializer.data)


@api_view(['PATCH'])
def change_password(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=400)

    serializer = ChangePasswordSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response()
    else:
        return Response(data=serializer.errors, status=400)


@api_view(['POST'])
def request_reset_password(request):
    try:
        user = User.objects.get(email=request.data["email"])
    except User.DoesNotExist:
        return Response()

    data = {"reset_token": str(uuid.uuid4()), "reset_time": datetime.datetime.now()}
    serializer = RequestResetPasswordSerializer(instance=user, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response()


@api_view(['POST'])
def verify_token(request):
    try:
        User.objects.get(reset_token=request.data["reset_token"])
        return Response("Success")
    except User.DoesNotExist:
        return Response(status=400)


@api_view(['POST'])
def reset_password(request):
    user = User.objects.get(reset_token=request.data["reset_token"])
    # reset_time not considered for now
    data = {"password": request.data["password"], "reset_token": None}
    serializer = ResetPasswordSerializer(instance=user, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response()
    else:
        return Response(serializer.errors, status=400)
