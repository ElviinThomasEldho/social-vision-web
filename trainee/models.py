from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Trainee(models.Model):

    PURPOSE = (
        ('Computer', 'Computer'),
        ('Volunteer', 'Volunteer'),
        ('Academic', 'Academic'),
        ('Member', 'Member'),
        ('Tailoring', 'Tailoring'),
        ('English Speaking', 'English Speaking'),
    )

    MARTIAL_STATUS = (
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
        ('Single', 'Single'),
        ('Widow', 'Widow'),
    )

    CATEGORY = (
        ('General', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('EWS', 'EWS'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    )

    RELIGION = (
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Sikh', 'Sikh'),
        ('Isai', 'Isai'),
        ('Jain', 'Jain'),
        ('Other', 'Other'),
    )

    OCCUPATION = (
        ('Private Job', 'Private Job'),
        ('Government Employee', 'Government Employee'),
        ('Self Employed', 'Self Employed'),
        ('House Wife', 'House Wife'),
        ('Business', 'Business'),
    )

    EDUCATION = (
        ('Nil', 'Nil'),
        ('5th Grade', '5th Grade'),
        ('6th Grade', '6th Grade'),
        ('7th Grade', '7th Grade'),
        ('8th Grade', '8th Grade'),
        ('9th Grade', '9th Grade'),
        ('10th Grade', '10th Grade'),
        ('11th Grade', '11th Grade'),
        ('12th Grade', '12th Grade'),
        ('Graduate', 'Graduate'),
        ('Post Graduate', 'Post Graduate'),
    )

    DOCUMENT_TYPE = (
        ('Aadhaar Card', 'Aadhaar Card'),
        ('Voter Card', 'Voter Card'),
        ('PAN Card', 'PAN Card'),
        ('Ration Card', 'Ration Card'),
        ('Passport', 'Passport'),
        ('Driving License', 'Driving License'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    uniqueID = models.CharField('Unique ID', primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    purpose = models.CharField('Purpose', max_length=255, choices=PURPOSE, null=True)
    profilePicture = models.ImageField('Profile Picture',null=True)
    firstName = models.CharField('First Name', max_length=255, null=True)
    lastName = models.CharField('Last Name', max_length=255, null=True)
    fatherName = models.CharField("Father's Name", max_length=255, null=True)
    motherName = models.CharField("Mother's Name", max_length=255, null=True)

    dateOfBirth = models.DateField("Date of Birth", null=True)
    age = models.IntegerField("Age of Trainee", null=True)

    martialStatus = models.CharField('Martial Status', max_length=255, choices=MARTIAL_STATUS, null=True)
    category = models.CharField('Category', max_length=255, choices=CATEGORY, null=True)
    gender = models.CharField('Gender', max_length=255,choices=GENDER, null=True)
    religion = models.CharField('Religion', max_length=255, choices=RELIGION, null=True)

    mobileNumber = models.CharField('Mobile Number', max_length=13, null=True)
    emailID = models.EmailField('Email Address', null=True)
    emergencyContact = models.CharField('Emergency Contact', max_length=13, null=True)

    occupation = models.CharField('Occupation', max_length=255, choices=OCCUPATION, null=True)
    education = models.CharField('Education', max_length=255, choices=EDUCATION, null=True)
    address = models.CharField('Address', max_length=512, null=True)
    area = models.CharField('Area', max_length=255, null=True)
    locality = models.CharField('Locality', max_length=255, null=True)
    district = models.CharField('District', max_length=255, null=True)
    state = models.CharField('State', max_length=255, null=True)
    pincode = models.CharField('Pincode', max_length=255, null=True)

    documentType = models.CharField('Document Type', max_length=255, choices=DOCUMENT_TYPE, null=True)
    documentNumber = models.CharField('Document Number', max_length=255, null=True)
    
    signature = models.ImageField('Signature',null=True)

    dateCreated = models.DateTimeField(null=True, auto_now_add=True)

    # trainee photo
    # trainee signature

    declaration = models.BooleanField(
        'I hereby declare that the above particulars of facts and information stated are true, correct and complete to the best of my belief and knowledge', null=True)

    # captcha

    def __str__(self):
        return (self.uniqueID + " | " + self.firstName + ' ' + self.lastName)
