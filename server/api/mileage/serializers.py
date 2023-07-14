from .models import Mileage
from ..users.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['challenge_start_date']

class MileageSerializer(ModelSerializer):

    # user = UserSerializer()

    class Meta:
        model = Mileage
        fields = '__all__'
