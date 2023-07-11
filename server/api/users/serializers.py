from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

class UserSerialiser(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class ChangePasswordSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            # "id",
            "password"
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class RequestResetPasswordSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            # "email",
            "reset_token",
            "reset_time",
        ]


class ResetPasswordSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            # "id",
            "password",
            "reset_token",
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance