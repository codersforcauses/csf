from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import ChangePasswordSerializer, RequestResetPasswordSerializer, ResetPasswordSerializer, UserSerialiser
from django.core.mail import send_mail
from django.conf import settings


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
        send_mail(
            subject="Reset Password",
            message=make_reset_email_message(user.email, user.reset_token),
            from_email=settings.EMAIL_ADDRESS_FROM,
            recipient_list=[user.email],
            fail_silently=False,
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


def make_reset_email_message(email, token):
    return ("We have received a request to reset the password "
            f"for the Community Spirit Foundation account associated with {email}. "
            "No changes have been made to your account yet.\n"
            "If you did make this request, you should see a field in which to enter a token. "
            f"Paste the following token into the field to reset your password:\n\n{token}\n\n"
            "If you did not request a new password, please ignore this email.")
