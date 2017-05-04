from django.conf.urls import url
from .models import Meal
from .models import Order

urlpatterns = [
	url(r'^$', views.meal_details, name='meal_details'),
]