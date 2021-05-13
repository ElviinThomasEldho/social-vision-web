from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.regAssociate, name='regAssociate'),
    path('profile/', views.profAssociate, name='profAssociate'),

    path('expense/view/', views.viewExpense, name='viewExpense'),
    path('expense/add/', views.addExpense, name='addExpense'),
    path('expense/print/report/', views.printExpense, name='printExpense'),
    path('expense/print/receipt/<str:id>/', views.printExpReceipt, name='printExpReceipt'),

    path('revenue/view/', views.viewRevenue, name='viewRevenue'),
    path('revenue/add/', views.addRevenue, name='addRevenue'),
    path('revenue/print/report/', views.printRevenue, name='printRevenue'),
    path('revenue/print/receipt/<str:id>/', views.printRevReceipt, name='printRevReceipt'),
    
    path('service/add/', views.addService, name='addService'),
    path('service/print/receipt/<str:id>/', views.printServReceipt, name='printServReceipt'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)