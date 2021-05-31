from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('view/', views.profile, name='trainee'),
    path('register/', views.register, name='regTrainee'),
    path('edit/', views.edit, name='editTrainee'),
    path('pdf/', views.printForm, name='printTrainee'),
    path('id/', views.printID, name='printTraineeID'),

    path('activate/<str:id>/', views.activate, name='activateTrainee'),
    path('deactivate/<str:id>/', views.deactivate, name='deactivateTrainee'),
    path('enroll/<str:id>/', views.enroll, name='enroll'),
    path('unenroll/<str:id>/', views.unenroll, name='unenroll'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
