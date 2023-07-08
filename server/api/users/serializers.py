from rest_framework.serializers import ModelSerializer
from .models import User

class RequestResetPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "email"