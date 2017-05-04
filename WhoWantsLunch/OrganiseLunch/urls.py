from django.conf.urls import url
from . import views

url(r'^Lunch/', 'OrganiseLunch.Templates.Lunches', name = 'lunches'),