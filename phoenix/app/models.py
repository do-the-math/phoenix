import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


from phoenix.base_model import BasePhoenixModel
from phoenix.app.managers.user_manager import UserManager


def player_image_upload_path(i, f):
    return '/'.join(['drivers', str(i.pk), 'image.jpg'])


class User(AbstractUser, BasePhoenixModel):

    site = models.ForeignKey(Site,
                             default=settings.SITE_ID,
                             on_delete=models.CASCADE)
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        get_latest_by = 'created_at'
        ordering = ('-created_at',)
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'site'], name='unique user per site'
            )
        ]

    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{}'.format(self.username)

    # objects = UserManager
