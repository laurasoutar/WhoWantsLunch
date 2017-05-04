from django.conf.urls import url
from OrganiseLunch.views import Lunches

urlpatterns = [
    url(r'lunches/$', Lunches, name="lunches"),
]