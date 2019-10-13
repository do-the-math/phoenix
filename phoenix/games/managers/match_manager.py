
from django.contrib.auth.models import EmptyManager
from django.db import models, transaction
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db import models


class MatchManager(models.Manager):
    use_in_migrations = True

    # @transaction.atomic
    # def save(self, *args, **kwargs):
    #     pass
