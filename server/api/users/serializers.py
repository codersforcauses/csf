from rest_framework.serializers import ModelSerializer
from .models import User


class ChangePasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            # "id",
            "password"
        ]


class RequestResetPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email"
        ]


class ResetPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "reset_token",
            "password"
        ]