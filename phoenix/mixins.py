from datetime import datetime
from decimal import Decimal
from uuid import UUID

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, Exists, OuterRef
from django.db.models.fields.files import ImageFieldFile
from django.utils.decorators import decorator_from_middleware
from django.utils.text import slugify
from django.http.response import HttpResponse

from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin
)


from .app.models import User


class PhoenixUpdateModelMixin(UpdateModelMixin):
    pass


class PhoenixCreateModelMixin(CreateModelMixin):
    pass


class PhoenixListModelMixin(ListModelMixin):
    pass


class PhoenixGenericViewSet(viewsets.GenericViewSet):
    def get_serializer(self, *args, **kwargs):
        if self.action in ['update', 'partial_update']:
            kwargs['partial'] = True
        serializer_class = self.get_serializer_class()
        if 'context' not in kwargs:
            kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ['update', 'partial_update', 'create'] and self.request.data:
            return getattr(self, 'create_update_serializer_class', self.serializer_class)
        return super().get_serializer_class(*args, **kwargs)
