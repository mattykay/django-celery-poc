from __future__ import absolute_import, unicode_literals

from django.conf.urls import handler404, handler500, include, url  # noqa

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.urls import path
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]
