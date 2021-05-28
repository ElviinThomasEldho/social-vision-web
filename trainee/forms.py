from django.forms import ModelForm, Textarea
from django.forms.widgets import Widget
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TraineeForm(ModelForm):
    class Meta:
        model = Trainee
        exclude = ['uniqueID', 'firstName', 'lastName', 'emailID', 'age', 'dateCreated', 'status',
                   'course', 'validUpto', 'enrolledCourses']

        widgets = {
            'user': forms.HiddenInput(),
            'purpose': forms.Select(),
            'fatherName': forms.TextInput(),
            'motherName': forms.TextInput(),

            'dateOfBirth': DateInput(),
            'bloodGroup': forms.Select(),

            'martialStatus': forms.Select(),
            'category': forms.Select(),
            'gender': forms.Select(),
            'religion': forms.Select(),

            'mobileNumber': forms.TextInput(),
            'emergencyContact': forms.TextInput(),

            'occupation': forms.Select(),
            'education': forms.Select(),
            'address': forms.Textarea(),
            'area': forms.TextInput(),
            'locality': forms.TextInput(),
            'district': forms.TextInput(),
            'state': forms.TextInput(),
            'pincode': forms.TextInput(),

            'documentType': forms.Select(),
            'documentNumber': forms.TextInput(),

            'declaration': forms.CheckboxInput(),
        }
