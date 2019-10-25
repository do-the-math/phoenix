from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core import serializers
from django.db.models import Q
from django.template.loader import get_template
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from phoenix.games.models import *
from phoenix.games.serializers import MatchSerializer


class MatchViewSet(viewsets.GenericViewSet):

    queryset = Match.objects.all()

    permission_classes_by_action = {
        'pusher_authentication': [permissions.AllowAny],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        # if self.action == 'current_user':
        return MatchSerializer

    @action(detail=False, methods=['post'])
    def pusher_authentication(self):
        pass
