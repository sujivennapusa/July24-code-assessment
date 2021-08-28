from django.db import models
class College(models.Model):
    name=models.CharField(max_length=50)
    admnno =models.IntegerField()
    rollno =models.IntegerField()
    college=models.CharField(max_length=25)
    parentname=models.CharField(max_length=50)
    mobilenumber=models.BigIntegerField()
    department1=models.CharField(max_length=50)
