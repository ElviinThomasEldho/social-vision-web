from django.forms import ModelForm, Textarea
from .models import *
from django import forms

class TraineeForm(ModelForm):
    class Meta:
        model = Trainee
        exclude = ['uniqueID','dateCreated']

        widgets = {
            'user' : forms.HiddenInput(),
            'purpose' : forms.Select(),
            'firstname' : forms.TextInput(),
            'lastName' : forms.TextInput(),
            'fatherName' : forms.TextInput(),
            'motherName' : forms.TextInput(),
            
            'dateOfBirth' : forms.DateInput(),
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
            
            'declaration' : forms.CheckboxInput(),  
        }