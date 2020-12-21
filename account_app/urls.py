from django.urls import path
from account_app import views

app_name = 'account'
urlpatterns = [
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('activate-account/<activate_code>', views.activate_account),
    path('forget-password', views.forget_password, name='forget_password'),
    path('reset-password/<activate_code>', views.reset_password, name='reset_password'),

]
