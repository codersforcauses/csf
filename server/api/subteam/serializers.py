from .models import SubTeam
from rest_framework.serializers import ModelSerializer


class SubTeamSerialiser(ModelSerializer):
    class Meta:
        model = SubTeam
        fields = '__all__'
