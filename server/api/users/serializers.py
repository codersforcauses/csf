from rest_framework import serializers

from . import User

class signup_modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
