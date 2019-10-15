from rest_framework import routers

from .views import (
    PhoenixAuthViewSet
)

api_router = routers.DefaultRouter()

api_router.register(r'auth', PhoenixAuthViewSet, 'auth')


urlpatterns = [
]
