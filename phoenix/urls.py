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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from phoenix.app.urls import api_router


admin.site.site_header = 'Phoenix Admin'
admin.site.site_title = 'Phoenix Admin'
admin.site.index_title = 'Phoenix Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Include the rest of the ruckit app urls

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url('^__debug__/', include(debug_toolbar.urls))]
