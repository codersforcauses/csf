from .models import Mileage
from rest_framework.serializers import ModelSerializer


class MileageSerializer(ModelSerializer):
    class Meta:
        model = Mileage
        fields = '__all__'
