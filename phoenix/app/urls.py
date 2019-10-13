from django.conf.urls import url
from rest_framework import routers

from .views import (
    PhoenixAuthViewSet
)

api_router = routers.DefaultRouter()

api_router.register(r'auth', PhoenixAuthViewSet, 'auth')
# api_router.register(r'users', UserViewSet, 'user')


urlpatterns = [
]
