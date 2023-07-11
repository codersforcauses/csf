from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import ChangePasswordSerializer, RequestResetPasswordSerializer, ResetPasswordSerializer, UserSerialiser
# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError

import uuid, datetime

@api_view(['GET'])
def get_user(request, username):
    user = User.objects.get(username=username)
    serializer = UserSerialiser(user)
    return Response(serializer.data)

@api_view(['PATCH'])
def change_password(request, id):
    user = User.objects.get(id=id)
    serializer = ChangePasswordSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response()

@api_view(['POST'])
def request_reset_password(request):
    try:
        user = User.objects.get(email=request.data["email"])
        data = {"reset_token": str(uuid.uuid4()), "reset_time": datetime.datetime.now()}
        serializer = RequestResetPasswordSerializer(instance=user, data=data)
        if serializer.is_valid():
            serializer.save()

            # should be an empty response and reset_token only sent in email
            return Response({"reset_token": data["reset_token"]})
    except:
        return Response()
    
@api_view(['POST'])
def verify_token(request):
    try:
        user = User.objects.get(reset_token=request.data["reset_token"])
        return Response("Success")
    except:
        return Response("Invalid")
    
@api_view(['POST'])
def reset_password(request):
    user = User.objects.get(reset_token=request.data["reset_token"])
    # reset_time not considered for now
    data = { "password": request.data["password"], "reset_token": None }
    serializer = ResetPasswordSerializer(instance=user, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response("Success")
    else:
        return Response(serializer.errors)
