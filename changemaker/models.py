from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class ChangeMaker(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    )

    DOCUMENT_TYPE = (
        ('Aadhaar Card', 'Aadhaar Card'),
        ('Voter Card', 'Voter Card'),
        ('PAN Card', 'PAN Card'),
        ('Ration Card', 'Ration Card'),
        ('Passport', 'Passport'),
        ('Driving License', 'Driving License'),
    )

    PURPOSE = (
        ('Donation', 'Donation'),
        ('Education', 'Education'),
        ('Differently Abled', 'Differently Abled'),
        ('Medical Aid', 'Medical Aid'),
        ('Ration Support', 'Ration Support'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Skill Developement', 'Skill Developement'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    uniqueID = models.CharField('Unique ID', primary_key=True, default=uuid.uuid4(
    ).hex[:5].upper(), max_length=50, editable=False)
    profilePicture = models.ImageField('Profile Picture', null=True)
    firstName = models.CharField('First Name', max_length=255, null=True)
    lastName = models.CharField('Last Name', max_length=255, null=True)
    fatherName = models.CharField("Father's Name", max_length=255, null=True)

    dateOfBirth = models.DateField("Date of Birth", null=True)
    age = models.IntegerField("Age of Candidate", null=True)

    gender = models.CharField('Gender', max_length=255,
                              choices=GENDER, null=True)

    mobileNumber = models.CharField('Mobile Number', max_length=13, null=True)
    emailID = models.EmailField('Email Address', null=True)
    emergencyContact = models.CharField(
        'Emergency Contact Number', max_length=13, null=True)

    address = models.CharField('Address', max_length=512, null=True)
    area = models.CharField('Area', max_length=255, null=True)
    locality = models.CharField('Locality', max_length=255, null=True)
    district = models.CharField('District', max_length=255, null=True)
    state = models.CharField('State', max_length=255, null=True)
    pincode = models.CharField('Pincode', max_length=255, null=True)

    # Monthly Donations
    isMonthly = models.BooleanField(
        'Is Monthly', null=True, default=False)
    monthlyAmount = models.IntegerField('Monthly Donation Amount', null=True)
    monthlyPurpose = models.CharField(
        'Purpose of Donation', max_length=25, choices=PURPOSE, null=True)
    goldenDate = models.IntegerField(
        'Golden Date of Giving', null=True)
    autoDebiting = models.BooleanField(
        'Auto-Debiting', null=True, default=False)

    documentType = models.CharField(
        'Document Type', max_length=255, choices=DOCUMENT_TYPE, null=True)
    documentNumber = models.CharField(
        'Document Number', max_length=255, null=True)

    dateCreated = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return (self.uniqueID + " | " + self.firstName + ' ' + self.lastName)


class Donation(models.Model):

    PURPOSE = (
        ('Donation', 'Donation'),
        ('Education', 'Education'),
        ('Differently Abled', 'Differently Abled'),
        ('Medical Aid', 'Medical Aid'),
        ('Ration Support', 'Ration Support'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Skill Developement', 'Skill Developement'),
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    uniqueID = models.CharField('studentID', primary_key=True, default=uuid.uuid4(
    ).hex[:5].upper(), max_length=50, editable=False)
    amount = models.IntegerField('Donation Amount', null=True)
    purpose = models.CharField(
        'Purpose', max_length=255, choices=PURPOSE, null=True)
    status = models.CharField(
        'Donation Status', max_length=255, choices=STATUS, null=True, default="Pending")

    isMonthly = models.BooleanField(
        'Monthly Donation', null=True, default=False)

    dateCreated = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return (self.user.username + " | " + self.purpose)
