from django.db.models.base import Model
from .models import Event
from rest_framework.serializers import ModelSerializer


class EventSerialiser(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
