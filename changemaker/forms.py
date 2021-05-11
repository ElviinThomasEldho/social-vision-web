from django.forms import ModelForm, Textarea
from .models import *
from django import forms

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        exclude = ['uniqueID','status']

        widgets = {
            'user' : forms.HiddenInput(),
            'amount' : forms.TextInput(),
            'purpose' : forms.Select(),
        }