from django.db.models import Q
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from rest_framework import serializers

# from phoenix.app.models import User


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        depth = 1
        exclude = [
            'password',
        ]


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'site',
            'password'
        ]

    def validate_password(self, value):
        if(len(value) < 7):
            raise serializers.ValidationError("Password less than 7")
        return value


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    site = serializers.CharField(required=True)
