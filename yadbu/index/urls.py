from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index_view, name= 'index_view'),
    path('columns/', views.columns, name= 'columns')
]

