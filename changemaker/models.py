from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Donation(models.Model):

    PURPOSE = (
        ('Donation','Donation'),
        ('Education','Education'),
        ('Differently Abled','Differently Abled'),
        ('Medical Aid','Medical Aid'),
        ('Ration Support','Ration Support'),
        ('Women Empowerment','Women Empowerment'),
        ('Skill Developement','Skill Developement'),
    )

    STATUS = (
        ('Pending','Pending'),
        ('Completed','Completed'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    uniqueID = models.CharField('studentID', primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    amount = models.IntegerField('Donation Amount',null=True)
    purpose = models.CharField('Purpose', max_length=255, choices=PURPOSE, null=True)
    status = models.CharField('Donation Status', max_length=255, choices=STATUS, null=True, default="Pending")

    dateCreated = models.DateTimeField(null=True, auto_now_add=True)


    def __str__(self):
        return (self.uniqueID + " | " + self.user.username + " | " + self.purpose)
