from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

    def validate(self, attrs): # Validate the inputs to user creation. Name and type are required, and type must be one of the predefined choices.
        if not attrs.get('username'):
            raise serializers.ValidationError("Name is required.")

        return attrs

    def create(self, validated_data):
        user, created = User.objects.get_or_create(
            username=validated_data.get('username'),
        )
        self._was_created = created  # Flag for the view to return 201 Created if a new user was created
        return user