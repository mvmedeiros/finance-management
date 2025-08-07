from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

    def validate_username(self, value):
        return value.title()

    def create(self, validated_data):
        user, created = User.objects.get_or_create(
            username = validated_data['username'],
        )
        self._was_created = created  # Flag for the view to return 201 Created if a new user was created
        return user