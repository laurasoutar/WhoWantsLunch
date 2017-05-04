from django.conf.urls import url
from Lunches import OrganiseLunch.views

urlpatterns = [
    url(r'lunches/$', Lunches, name="lunches"),
]