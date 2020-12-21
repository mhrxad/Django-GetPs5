from django.contrib import admin
from django.urls import path

from contactus_app import views

app_name = 'contact_us'
urlpatterns = [
    path('contact-us', views.contact_us, name='contact_us'),
]
