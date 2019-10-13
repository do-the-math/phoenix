import logging
# import rollbar
import sys
import time

from django.conf import settings
from django.http.response import (Http404, HttpResponseBadRequest,
                                  HttpResponseNotFound)
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
