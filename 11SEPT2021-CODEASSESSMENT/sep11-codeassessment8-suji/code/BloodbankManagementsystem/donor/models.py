from django.db import models

# Create your models here.
class Donor(models.Model):
    name=models.CharField(max_length=50,default='', blank=True)
    address=models.CharField(max_length=50,default='', blank=True)
    bloodgroup=models.CharField(max_length=50,default='', blank=True)
    mobileno=models.CharField(max_length=50,default='', blank=True)
    username=models.CharField(max_length=50,default='', blank=True)
    password=models.CharField(max_length=50,default='', blank=True)
class Blogs(models.Model):
    donorid = models.IntegerField()
    donordata=models.CharField(max_length=400,default='',blank=True)    