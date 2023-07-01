from .models import Team
#!!
from rest_framework.serializers import ModelSerializer

class TeamSerialiser(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'