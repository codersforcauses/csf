from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import (ChangeDetailsSerializer, ChangePasswordSerializer, RequestResetPasswordSerializer, 
                          ResetPasswordSerializer, JoinTeamSerializer, PublicUserSerializer)
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.hashers import check_password

from ..team.models import Team


import uuid
import datetime


@api_view(['GET'])
def get_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=400)
    serializer = PublicUserSerializer(user)
    return Response(serializer.data)


@api_view(['PATCH'])
def change_details(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=400)
    serializer = ChangeDetailsSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response()
    else:
        return Response(data=serializer.errors, status=400)


@api_view(['PATCH'])
def change_password(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=400)
    if not check_password(request.data["old_password"], user.password):
        return Response(data={"old_password": "Incorrect password"}, status=400)

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
        html_content = render_to_string('reset_password.html', {'token': user.reset_token, 'username': user.username, 'email': user.email})
        send_mail(
            subject="Reset Password",
            message=make_reset_email_message(user.email, user.username, user.reset_token),
            from_email=settings.EMAIL_ADDRESS_FROM,
            recipient_list=[user.email],
            fail_silently=False,
            html_message=html_content
        )

    return Response()


@api_view(['POST'])
def verify_token(request):
    if request.data["reset_token"] != "":
        try:
            User.objects.get(reset_token=request.data["reset_token"])
            return Response("Success")
        except User.DoesNotExist:
            return Response(status=400)
    else:
        return Response(status=400)


@api_view(['POST'])
def reset_password(request):
    if request.data["reset_token"] != "":
        user = User.objects.get(reset_token=request.data["reset_token"])
        # reset_time not considered for now
        data = {"password": request.data["password"], "reset_token": ""}
        serializer = ResetPasswordSerializer(instance=user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response(status=400)


def make_reset_email_message(email, username, token):
    return (f"Hi {username},\nWe have received a request to reset the password "
            f"for the Community Spirit Foundation account associated with {email}. "
            "No changes have been made to your account yet.\n"
            "If you did make this request, you should see a field in which to enter a token. "
            f"Paste the following token into the field to reset your password:\n\n{token}\n\n"
            "If you did not request a new password, please ignore this email.")


@api_view(['PATCH'])
def join_team(request, id):
    user = User.objects.get(id=id)
    team = Team.objects.get(join_code=request.data['join_code'])

    data = {
        'team_id': team.team_id,
        'team_admin': request.data['team_admin']
    }

    user_serializer = JoinTeamSerializer(instance=user, data=data)

    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data)
    else:
        return Response(user_serializer.errors, status=400)


@api_view(['PATCH'])
def remove_team(request, id):
    user = User.objects.get(id=id)

    data = {
        'team_id': None,
        'team_admin': False
    }

    user_serializer = JoinTeamSerializer(instance=user, data=data)

    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data)
    else:
        return Response(user_serializer.errors, status=400)
