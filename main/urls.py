from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('covid-help/', views.covid, name='covid'),
    path('donate/', views.donate, name='donate-1'),
    
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('profile/', views.profileUser, name='profile'),
]
