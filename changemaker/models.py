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

    isVolunteer = models.BooleanField(
        'Is Volunteer', null=True, default=False)

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

class Skill(models.Model):

    name = models.CharField('Skill', max_length=25, null=True)

    def __str__(self):
        return (self.name)
        
class Interest(models.Model):

    name = models.CharField('Interest', max_length=25, null=True)

    def __str__(self):
        return (self.name)

class Volunteer(models.Model):
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

    DURATION = (
        ('1 Year','1 Year'),
        ('5 Year','5 Year'),
        ('10 Year','10 Year'),
        ('Lifetime','Lifetime'),
    )

    INTEREST = (
        ('Helping Children','Helping Children'),
        ('Helping Youth','Helping Youth'),
        ('Helping Organization in Technical Work','Helping Organization in Technical Work'),
        ('Helping in Communication Work','Helping in Communication Work'),
        ('Overall help','Overall help'),
        ('Helping Divyang','Helping Divyang'),
    )

    changemaker = models.ForeignKey(ChangeMaker, null=True, on_delete=models.SET_NULL)
    education = models.CharField('Education',max_length=25, null=True, choices=EDUCATION)
    specialization = models.CharField('Specialization',null=True, max_length=250)
    skills = models.ManyToManyField(Skill)
    interests = models.ManyToManyField(Interest)
    duration = models.CharField('Duration',max_length=25, choices=DURATION, null=True)
    hours = models.IntegerField('Volunteering Hours', null=True)

    def __str__(self):
        return (self.changemaker.firstName + ' ' + self.changemaker.lastName)