from django.forms import ModelForm, Textarea
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ChangeMakerForm(ModelForm):
    class Meta:
        model = ChangeMaker
        exclude = ['uniqueID','dateCreated']

        widgets = {
            'user' : forms.HiddenInput(),
            'firstname' : forms.TextInput(),
            'lastName' : forms.TextInput(),
            'fatherName' : forms.TextInput(),
            'motherName' : forms.TextInput(),
            
            'dateOfBirth' : DateInput(),
            'age' : forms.NumberInput(),
            
            'martialStatus' : forms.Select(attrs={'width':'100px'}),
            'category' : forms.Select(),
            'gender' : forms.Select(),
            'religion' : forms.Select(),
    
            'mobileNumber' : forms.TextInput(),
            'emailID' : forms.EmailInput(),
            'emergencyContact' : forms.TextInput(),
            
            'occupation' : forms.Select(),
            'education' : forms.Select(),
            'address' : forms.Textarea(),
            'area' : forms.TextInput(),
            'locality' : forms.TextInput(),
            'district' : forms.TextInput(),
            'state' : forms.TextInput(),
            'pincode' : forms.TextInput(),
            'documentType' : forms.Select(),
            'documentNumber' : forms.TextInput(),
        }


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        exclude = ['uniqueID','status']

        widgets = {
            'user' : forms.HiddenInput(),
            'amount' : forms.TextInput(),
            'purpose' : forms.Select(),
        }