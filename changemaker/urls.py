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

    path('monthly-create/', views.monthlyDonationForm, name='donateMonthlyForm'),
    path('monthly-pay/<str:id>/', views.paymentMonthly, name='donateMonthlyPay'),
    path('monthly-success/<str:id>/', views.paymentMonthlySuccess,
         name='donateMonthlySuccess'),
    path('monthly-certificate/<str:id>/',
         views.printMonthlyCertificate, name='printMonthlyDonCertif'),
    path('monthly-receipt/<str:id>/', views.printMonthlyReceipt,
         name='printMonthlyDonReceipt'),
]
