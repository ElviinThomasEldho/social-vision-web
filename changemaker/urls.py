from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('view/', views.donateView, name='donate'),
    path('create/', views.donateForm, name='donateForm'),
    path('pay/<str:id>/', views.donatePay, name='donatePay'),
    path('success/<str:id>/', views.donateSuccess, name='donateSuccess'),
    path('certificate/<str:id>/', views.printDonationCertif, name='printDonCertif'),
    path('receipt/<str:id>/', views.printDonationReceipt, name='printDonReceipt'),
]
