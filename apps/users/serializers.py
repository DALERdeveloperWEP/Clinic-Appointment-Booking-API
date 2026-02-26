from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=24)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=16)
    confirm = serializers.CharField(min_length=8, max_length=16)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise ValidationError({"confirm": "Password and confirm password do not match."})
        return super().validate(attrs)
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
