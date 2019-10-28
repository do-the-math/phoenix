import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

from phoenix.accounts.models import BasePhoenixModel, User


class Category(BasePhoenixModel):
    name = models.CharField(default="Category Name")
    created_by = models.ForeignKey("User",
                                   on_delete=models.CASCADE)

    class Meta:
        get_latest_by = 'created_at'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.name)


class Contact(BasePhoenixModel):
    name = models.CharField(default="Contact Name")
    user = models.OneToOneField("User",
                                on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    marker = models.OneToOneField("Marker", on_delete=models.PROTECT)
    notes = models.ManyToManyField("Note", on_delete=models.PROTECT)

    class Meta:
        get_latest_by = 'created_at'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.name)


class Marker(BasePhoenixModel):
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    address_string = models.TextField(default="ext")

    class Meta:
        get_latest_by = 'created_at'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.name)


class Note(BasePhoenixModel):
    text = models.TextField(default="dsfsdf")

    class Meta:
        get_latest_by = 'created_at'
        ordering = ('-created_at',)

    def __str__(self):
        return '{}'.format(self.text[0:10])
