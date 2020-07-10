from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import wildcard_redirect

urlpatterns = [
    url(r'^(?P<path>.*)', wildcard_redirect),
]
