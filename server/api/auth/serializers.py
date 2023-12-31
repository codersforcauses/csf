from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class SignUpmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'team_signup', 'has_consent', 'travel_method', 'avatar']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'allow_blank': False},
            'last_name': {'allow_blank': False}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
