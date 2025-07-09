from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'type']
        
    
    def validate(self, attrs): # Validate the inputs to category creation. Name and type are required, and type must be one of the predefined choices.
        if not attrs.get('name'):
            raise serializers.ValidationError("Name is required.")
        if not attrs.get('type'):
            raise serializers.ValidationError("Type is required.")
        if attrs['type'] not in dict(Category.TYPE_CHOICES):
            raise serializers.ValidationError(f"Invalid type: {attrs['type']}. Must be one of {dict(Category.TYPE_CHOICES).keys()}.")
        return attrs