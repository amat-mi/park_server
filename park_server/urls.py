# coding: utf-8

from django.conf import settings
from django.conf.urls import patterns, url, include, static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rtpark/', include('park_server_core.urls')),
)

# urlpatterns = format_suffix_patterns(urlpatterns)
# 
# urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
