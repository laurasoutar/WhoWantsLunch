from django.conf.urls import url
from OrganiseLunch.views import lunches, order_view, home, meal_view

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'lunches/$', lunches, name="lunches"),
    url(r'meal_setup/$', meal_view, name="meal_setup"),
    url(r'lunches/(\d+)/order', order_view, name="order_meal")
]