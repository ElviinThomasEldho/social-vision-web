from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('view/', views.profile, name='donate'),
    path('register/', views.register, name='regChangeMaker'),
    path('create/', views.donationForm, name='donateForm'),
    path('pay/<str:id>/', views.payment, name='donatePay'),
    path('success/<str:id>/', views.paymentSuccess, name='donateSuccess'),
    path('certificate/<str:id>/', views.printCertificate, name='printDonCertif'),
    path('receipt/<str:id>/', views.printReceipt, name='printDonReceipt'),
]
