# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=140, default='')
    contact_number = models.CharField(max_length=140, default='')
    State = models.CharField(max_length=140, default='')
    Country = models.CharField(max_length=140, default='')
    DOB = models.DateField(("DOB"), default=datetime.date.today) 

class SubmissionForm(models.Model):
    title= models.CharField(max_length=1000)
    essay= models.CharField(max_length=10000)


def __str__(self):
  return self.user.username