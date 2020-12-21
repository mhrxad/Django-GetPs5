from django.urls import path
from faq_app import views

app_name = 'faq'
urlpatterns = [
    path('faqs', views.faqs, name='faqs'),
    path('faq/<faq_id>', views.faq_detail, name='faq_detail'),
]
