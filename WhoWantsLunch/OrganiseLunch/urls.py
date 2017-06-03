from django.conf.urls import url
from OrganiseLunch.views import get_slack_channels, home, lunch, lunches, meal_view, order_view

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'get_slack_channels/$', get_slack_channels, name="get_slack_channels"),
    url(r'lunch/(\d+)/$', lunch, name="lunch"),
    url(r'lunches/$', lunches, name="lunches"),
    url(r'meal_setup/$', meal_view, name="meal_setup"),
    url(r'lunches/(\d+)/order', order_view, name="order_meal")
]