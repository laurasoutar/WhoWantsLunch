from django.conf.urls import url
from OrganiseLunch.views import Lunches, Order, Home

urlpatterns = [
	url(r'^$', Home, name="home"),
    url(r'lunches/$', Lunches, name="lunches"),
    url(r'lunches/(\d+)/order', Order, name="order_meal")