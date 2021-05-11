from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('view/', views.traineeProfile, name='trainee'),
    path('register/', views.regTrainee, name='regTrainee'),
    path('edit/', views.editTrainee, name='editTrainee'),
    path('pdf/', views.printTraineeForm, name='printTrainee'),
    path('id/', views.printTraineeID, name='printTraineeID'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
