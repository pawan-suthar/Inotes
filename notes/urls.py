
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login', userlogin, name='userlogin'),
    path('logout', Logout, name='logout'),
    path('signin', signin, name='signin'),
    path('login_admin', login_admin, name='login_admin'),
    path('home_admin', home_admin, name='home_admin'),

]
