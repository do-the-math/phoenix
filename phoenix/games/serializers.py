from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db.models import Q
from rest_framework import serializers

from phoenix.games.models import Match


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'
