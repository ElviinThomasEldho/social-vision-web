from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
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

    # Reset Password
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='main/passwordReset.html'),
         name='reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='main/passwordResetSent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='main/passwordResetConfirm.html'),
         name='password_reset_confirm'),
    path('reset-password-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='main/passwordResetComplete.html'), name='password_reset_complete'),

    path('profile/', views.profile, name='profile'),
    path('finance/', views.finance, name='finance'),

    path('admin-panel/', views.panel, name='panel'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
