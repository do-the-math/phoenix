import uuid

from django.db import models


class BasePhoenixModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, db_index=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

    def __repr__(self):
        return '{}:{}'.format(self.pk.hex, self.__class__)
