from django.db.models import Q
from django.conf import settings
from django.core import serializers
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics, mixins, status


from phoenix.games.models import *
from phoenix.games.serializer import GameSerializer


import os
import json


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
        return GameSerializer

    @action(detail=False, methods=['post'])
    def pusher_authentication(self):
        pass

    # @transaction.atomic
    # def save(self, *args, **kwargs):
    #     # pp = self.players

    #     pp = self.players.all()
    #     players_count = len(self.players.select_for_update().all())
    #     if players_count > 2:
    #         raise ValidationError(
    #             ('Cannot Add More than Two Players')
    #         )
    #     else:
    #         pp = pp[0]
    #         self.winner = pp.player
    #         super(Match, self).save(*args, **kwargs)
