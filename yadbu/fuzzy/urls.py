from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
urlpatterns = [
    path('auto/', views.search_autocomplete, name = 'autocomplete')
]

