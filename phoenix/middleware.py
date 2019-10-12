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

# from rollbar.contrib.django.middleware import RollbarNotifierMiddleware
# from ruckit.stats import statsd

logger = logging.getLogger('sumoLogger')


class RuckitNotifierMiddleware(RollbarNotifierMiddleware):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        request.ruckit_body = request.body  # Cache the body so we can log if needed


class RuckitApiVersionMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        response['MIN_ANDROID_VERSION'] = settings.MIN_ANDROID_VERSION
        return response


METHOD_OVERRIDE_HEADER = 'HTTP_X_HTTP_METHOD_OVERRIDE'


class RuckitMethodOverrideMiddleware(MiddlewareMixin):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.method != 'POST':
            return
        if METHOD_OVERRIDE_HEADER not in request.META:
            return
        request.method = request.META[METHOD_OVERRIDE_HEADER]


class RequestLogMiddleware(MiddlewareMixin):
    '''Not reaaaally a middleware, just used for
    rest framework api request logging
    '''

    def process_request(self, request):
        request.start_time = time.time()
        try:
            # Cache the body so we can log if needed, but don't log multipart form
            request.ruckit_body = 'multipart/form-data' if request.content_type == 'multipart/form-data' else request.body
        except Exception:
            request.ruckit_body = None

    def process_response(self, request, response):
        if response.get('content-type', '') == 'application/json':
            if getattr(response, 'streaming', False):
                response_body = '<<<Streaming>>>'
            else:
                response_body = response.content
        else:
            response_body = '<<<Not JSON>>>'

        log_data = {
            'user': request.user,
            'remote_address': request.META['REMOTE_ADDR'],
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_body': request.ruckit_body,
            'response_status': response.status_code,
            'response_body': response_body,
            'run_time': time.time() - request.start_time,
        }

        # save log_data in some way
        logger.info(log_data)

        return response


class DeviceIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.device_id = request.META.get('HTTP_DEVICE_ID')
        response = self.get_response(request)
        return response
