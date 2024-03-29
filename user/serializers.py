from rest_framework import serializers
from .models import PassengerUser

# class RegisterFormSerializer(serializers.Serializer):
#     class Meta:
#         fields = ['phone', 'email', 'password1', 'password2']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerUser
        fields = ['email', 'phone', 'password']