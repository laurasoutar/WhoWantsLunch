from django.conf.urls import url
from . import callback, views

urlpatterns = [
    url(r'^callback/$', callback.process),
    url(r'^oauth/$', views.oauth),
]
