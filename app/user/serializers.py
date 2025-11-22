

from core.models import User
from rest_framework import serializers





class UserSerializer(serializers.ModelSerializer):
    """Serializer a user object"""

    password = serializers.CharField(write_only=True,
                                     style={'input_type':'password'},
                                     min_length = 8)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['name'],
            validated_data['password']
        )
        return user


    def update(self, instance, validated_data):
        """Handle updating user password senario"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)