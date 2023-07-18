from .models import Mileage
from ..users.models import User
from ..team.models import Team
from rest_framework.serializers import ModelSerializer, ValidationError

import datetime


class MileageSerializer(ModelSerializer):
    class Meta:
        model = Mileage
        fields = '__all__'

    def validate_date(self, date):
        if date > datetime.date.today():
            raise ValidationError("Date cannot be in the future.")
        return date


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'challenge_start_date']


class UserLeaderboardSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','total_mileage']

class TeamLeaderboardSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['name','bio','total_mileage']


# class PostMileageSerializer(ModelSerializer):

#     user = UserSerializer()

#     class Meta:
#         model = Mileage
#         fields = '__all__'
