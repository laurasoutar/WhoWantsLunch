from django.conf.urls import url
from OrganiseLunch.views import Lunches, OrderView, Home, meal_view

urlpatterns = [
	url(r'^$', Home, name="home"),
    url(r'lunches/$', Lunches, name="lunches"),
	url(r'meal_setup/$', meal_view, name="meal_setup"),
    url(r'lunches/(\d+)/order', OrderView, name="order_meal")
]