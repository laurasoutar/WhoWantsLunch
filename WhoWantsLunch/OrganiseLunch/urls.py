from django.conf.urls import url
from OrganiseLunch.views import Lunches, Home

urlpatterns = [
	url(r'^$', Home, name="home"),
    url(r'lunches/$', Lunches, name="lunches"),
]