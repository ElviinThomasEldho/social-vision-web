from django.forms import ModelForm, Textarea
from .models import *
from django import forms

class AssociateForm(ModelForm):
    class Meta:
        model = Associate
        exclude = ['uniqueID','dateCreated']

        widgets = {
            'user' : forms.Select(),
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
        }

class RevenueForm(ModelForm):
    class Meta:
        model = Revenue
        exclude = ['uniqueID','dateCreated']

        widgets = {
            'user' : forms.HiddenInput(),
            'firstname' : forms.TextInput(),
            'lastName' : forms.TextInput(),
    
            'mobileNumber' : forms.TextInput(),
            'emailID' : forms.EmailInput(),
            
            'address' : forms.Textarea(),
            'area' : forms.TextInput(),
            'locality' : forms.TextInput(),
            'district' : forms.TextInput(),
            'state' : forms.TextInput(),
            'pincode' : forms.TextInput(),

            'mode' : forms.Select(),
            'amount' : forms.NumberInput(),
            'PANNo' : forms.TextInput(),
            'AadhaarNo' : forms.TextInput(),

            'purpose' : forms.Select(),
        }

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['uniqueID','dateCreated']

        widgets = {
            'user' : forms.HiddenInput(),
            'firstname' : forms.TextInput(),
            'lastName' : forms.TextInput(),
    
            'mobileNumber' : forms.TextInput(),
            'emailID' : forms.EmailInput(),
            
            'address' : forms.Textarea(),
            'area' : forms.TextInput(),
            'locality' : forms.TextInput(),
            'district' : forms.TextInput(),
            'state' : forms.TextInput(),
            'pincode' : forms.TextInput(),

            'mode' : forms.Select(),
            'amount' : forms.NumberInput(),
            'PANNo' : forms.TextInput(),
            'AadhaarNo' : forms.TextInput(),

            'purpose' : forms.Select(),
            'service' : forms.Select(),
        }

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        exclude = ['uniqueID','dateCreated']

        widgets = {
            'user' : forms.HiddenInput(),
            'payeeName' : forms.TextInput(),

            'mobileNumber' : forms.TextInput(),

            'mode' : forms.Select(),
            'amount' : forms.NumberInput(),
            'PANNo' : forms.TextInput(),
            'AadhaarNo' : forms.TextInput(),

            'project' : forms.Select(),
            'budgetHead' : forms.Select(),
        }