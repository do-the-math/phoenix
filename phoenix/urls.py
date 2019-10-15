"""phoenix URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.urls import path, re_path, include, reverse_lazy


from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

from phoenix.accounts.views import PhoenixAuthViewSet

admin.site.site_header = 'Phoenix - Admin'

router = DefaultRouter()
router.register(r'users', PhoenixAuthViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^spec/', include_docs_urls(title='Phoenix API Docs', public=False)),

    url(r'^api/(?P<version>(v1))/', include(router.urls)),
    path('api/', RedirectView.as_view(url='/api/v1/')),

    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # default route - admin
    path('*', RedirectView.as_view(url='/admin/')),
]

# Only add if DEBUG
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
