from django.contrib import admin
from django.urls import path
from aboutus_app import views

app_name = 'about_us'
urlpatterns = [
    path('about-us', views.about_us, name='about_us'),
]
