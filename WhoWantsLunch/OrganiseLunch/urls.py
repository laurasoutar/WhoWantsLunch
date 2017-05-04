from django.conf.urls import url
from OrganiseLunch.views import Lunches, Order, Home, meal_view

urlpatterns = [
	url(r'^$', Home, name="home"),
    url(r'lunches/$', Lunches, name="lunches"),
	url(r'meal_setup/$', meal_view, name="meal_setup"),
    url(r'lunches/(\d+)/order', Order, name="order_meal")
]