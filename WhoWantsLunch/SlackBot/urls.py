from django.conf.urls import url
from . import callback

urlpatterns = [
    url(r'^callback/$', callback.process),
]
