from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('trainee/',include('trainee.urls')),
    path('change-maker/',include('changemaker.urls')),
    path('associate/',include('associate.urls')),
]   
