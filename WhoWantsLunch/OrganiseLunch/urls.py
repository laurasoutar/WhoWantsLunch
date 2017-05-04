from django.conf.urls import url
from OrganiseLunch.views import Lunches
from OrganiseLunch.views import meal_view

urlpatterns = [
    url(r'lunches/$', Lunches, name="lunches"),
	url(r'meal_setup/$', meal_view, name="meal")
]