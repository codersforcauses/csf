from rest_framework.serializers import ModelSerializer
from .models import User


class ChangePasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "password"


class RequestResetPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "email"


class ResetPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "reset_token", "password"