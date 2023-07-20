from .models import Event
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from datetime import date


class EventSerialiser(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise ValidationError('Event start date must be before start date')
        if data['start_date'] < date.today():
            raise ValidationError('Event cannot be created with a start date in the past')
        return data
