from rest_framework import serializers

from .models import User

class SignUpmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'team_signup', 'has_consent', 'travel_method']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            team_signup=self.validated_data['team_signup'],
            has_consent=self.validated_data['has_consent'],
            travel_method=self.validated_data['travel_method'],

        )
        password = self.validated_data['password']
        # confirm_password = self.validated_data['confirm_password']
        # if password != confirm_password:
        #     raise serializers.ValidationError({'password': 'The Password do not match.'})
        user.set_password(password)
        user.save()
        return user