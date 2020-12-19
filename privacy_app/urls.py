from django.contrib import admin
from django.urls import path
from privacy_app import views

app_name = 'privacy'
urlpatterns = [
    path('privacy', views.privacy, name='privacy'),
]
