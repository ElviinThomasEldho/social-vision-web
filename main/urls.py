from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('covid-help/', views.covid, name='covid'),
    path('donate/', views.donate, name='donate-1'),
    path('creating-impact/', views.impact, name='impact'),
    path('gallery/', views.gallery, name='gallery'),
    
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('finance/', views.finance, name='finance'),
    
    path('admin-panel/', views.panel, name='panel'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
