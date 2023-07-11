from .models import User
from rest_framework.serializers import ModelSerializer


class UserSerialiser(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
