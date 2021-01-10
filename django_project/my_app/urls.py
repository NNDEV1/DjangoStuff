from django.urls import path, include
from django.contrib import admin
from my_first_app import views

urlpatterns = [
    path('', views.index, name='index')
]
