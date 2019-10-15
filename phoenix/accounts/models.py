import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

# from phoenix.app.managers.user_manager import UserManager


def player_image_upload_path(i, f):
    return '/'.join(['drivers', str(i.pk), 'image.jpg'])


class BasePhoenixModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, db_index=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

    def __repr__(self):
        return '{}:{}'.format(self.pk.hex, self.__class__)


class User(AbstractUser, BasePhoenixModel):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    site = models.ForeignKey(Site,
                             default=settings.SITE_ID,
                             on_delete=models.CASCADE)

    class Meta:
        get_latest_by = 'created_at'
        ordering = ('-created_at',)
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'site'], name='one user per site'
            )
        ]

    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{}'.format(self.username)
