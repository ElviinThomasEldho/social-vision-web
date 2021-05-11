from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {     
            'username' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
        }



