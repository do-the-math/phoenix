from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


from .models import User
from .serializers import (
    UserSerializer,
    LoginSerializer,
    UserCreateSerializer
)


class PhoenixAuthViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    permission_classes_by_action = {
        'login': [permissions.AllowAny],
        'forgot_password': [permissions.AllowAny],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        return UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):

        serialized_input = self.get_serializer(data=request.data)
        serialized_input.is_valid(raise_exception=True)
        reuested_data = serialized_input.validated_data

        username = reuested_data.get('username').lower()
        password = reuested_data.get('password')
        site = get_current_site(request)

        try:
            user = User.objects.get(username=username, site=site)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                _user = UserSerializer(user).data
                response = {
                    "response": {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user': _user
                    }

                }
                return Response(response)
            else:
                return Response({'error': 'Wrong Password'}, status=status.HTTP_401_UNAUTHORIZED)

        except User.DoesNotExist:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
