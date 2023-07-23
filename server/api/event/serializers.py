from .models import Event
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from datetime import date


class EventSerialiser(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class CreateEventSerializer(EventSerialiser):

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise ValidationError('Event start date must be before start date')
        if data['start_date'] < date.today():
            raise ValidationError('Event cannot be created with a start date in the past')
        return data


class EditEventSerializer(EventSerialiser):

    def validate(self, data):
        if self.instance.start_date < date.today() and data['start_date'] != self.instance.start_date:
            raise ValidationError('You cannot modify the start date of an event after that start date has already occured')
        if self.instance.end_date < date.today() and data['end_date'] != self.instance.end_date:
            raise ValidationError('You cannot modify the end date of an event after that end date has already occured')
        if data['start_date'] > data['end_date']:
            raise ValidationError('Event start date must be before start date')
        return data
