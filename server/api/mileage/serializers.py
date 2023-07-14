from .models import Mileage
from ..users.models import User
from rest_framework.serializers import ModelSerializer


class MileageSerializer(ModelSerializer):
    class Meta:
        model = Mileage
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'challenge_start_date']


# class PostMileageSerializer(ModelSerializer):

#     user = UserSerializer()

#     class Meta:
#         model = Mileage
#         fields = '__all__'
