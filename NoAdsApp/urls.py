from django.contrib import admin
from django.urls import path, include, re_path
from NoAdsApp import views


app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('auth', views.auth, name='auth'),
    

]