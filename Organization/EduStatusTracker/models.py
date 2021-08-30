import uuid


# Create your models here.
from django.contrib.admin import options
from django.db import models


class Org_user_verification(models.Model):
    registrationID=models.IntegerField(primary_key=True,null=False)
    oneTimePassword=models.CharField(max_length=100)
    boardType=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    emailId=models.EmailField(max_length=254, null=True, blank=False, unique=False)
    is_FTL=models.IntegerField(default=0)
    password_exp_flag=models.BooleanField(default=True)
    dateCreated=models.DateField(auto_now_add=True)
    lastModifiedDate=models.DateField(auto_now_add=True)
    securityQuestionID=models.CharField(unique=True,blank=False,default=uuid.uuid4,max_length=100)  #will be unique
    authorizationID=models.IntegerField



class Org_security_question(models.Model):
    orgSecurityQueID = models.IntegerField(primary_key=True,default=uuid.uuid4)
    securityQuestionID = models.CharField(max_length=100)
    securityQuestion = models.CharField(max_length=100)
    securityAnswers = models.CharField(max_length=100)
    lastModifiedDate=models.DateField(auto_now_add=True)


class Org_authorization(models.Model):

    orgAuthorizationId=models.IntegerField(primary_key=True,default=uuid.uuid4)
    authorizationID = models.IntegerField
    authorizationType = models.CharField(blank=False,max_length=100)





