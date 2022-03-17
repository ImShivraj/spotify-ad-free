from django.contrib import admin
from django.urls import path, include, re_path
from NoAdsApp import views


app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('noadsapp', views.auth, name='auth'),
    

]