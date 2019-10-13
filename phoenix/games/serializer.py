from django.db.models import Q
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from rest_framework import serializers

from phoenix.app.models import User
from .models import Match


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'
