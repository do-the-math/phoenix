import os
from datetime import timedelta

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import LineString
from django.core.mail import send_mail
from django.db import connection, transaction
from django.db.models import F, Max, Q
from django.db.models.functions import Coalesce
from django.db.models.signals import (m2m_changed, post_delete, post_save,
                                      pre_delete, pre_save)
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created and not kwargs.get('raw', False):
#         Token.objects.create(user=instance)
