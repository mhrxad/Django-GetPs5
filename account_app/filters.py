import django_filters
from .models import User
from django import forms


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['gender', 'is_ban', 'is_active', 'email', 'username']
