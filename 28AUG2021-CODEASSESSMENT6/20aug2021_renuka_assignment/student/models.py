from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.CharField(max_length=50)
    admno=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    parentname=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=50)
    department=models.CharField(max_length=50)