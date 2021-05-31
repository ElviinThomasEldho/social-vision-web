from django.db.models import fields
from django.forms import ModelForm, Textarea
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class ChangeMakerForm(ModelForm):
    class Meta:
        model = ChangeMaker
        exclude = ['uniqueID', 'firstName', 'lastName',
                   'dateCreated', 'age', 'emailID', 'isMonthly', 'monthlyAmount', 'monthlyPurpose', 'goldenDate']

        widgets = {
            'user': forms.HiddenInput(),
            'fatherName': forms.TextInput(),

            'dateOfBirth': DateInput(),
            'gender': forms.Select(),

            'mobileNumber': forms.TextInput(),
            'emergencyContact': forms.TextInput(),

            'address': forms.Textarea(),
            'area': forms.TextInput(),
            'locality': forms.TextInput(),
            'district': forms.TextInput(),
            'state': forms.TextInput(),
            'pincode': forms.TextInput(),

            'documentType': forms.Select(),
            'documentNumber': forms.TextInput(),
        }


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        exclude = ['uniqueID', 'status']

        widgets = {
            'user': forms.HiddenInput(),
            'amount': forms.TextInput(),
            'purpose': forms.Select(),
        }


class monthlyDonationForm(ModelForm):
    class Meta:
        model = ChangeMaker
        fields = ['monthlyAmount', 'monthlyPurpose',
                  'goldenDate']

        widgets = {
            'monthlyAmount': forms.TextInput(),
            'monthlyPurpose': forms.Select(),
            'goldenDate': forms.TextInput(),
        }
