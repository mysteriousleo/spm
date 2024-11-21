from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Index"),
    path('check', views.checkSpam, name = "CheckSpam"),
]
