from django.conf.urls import url
from Lunches import views

urlpatterns = [
    url(r'lunches/$', Lunches, name="lunches"),
]