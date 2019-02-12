from django.contrib import admin
from django.urls import path, include
from fredapp.views import ChatterBotAppView, ChatterBotApiView
from . import views

urlpatterns = [
    path('', views.ChatterBotAppView, name='home'),
    path('api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]
