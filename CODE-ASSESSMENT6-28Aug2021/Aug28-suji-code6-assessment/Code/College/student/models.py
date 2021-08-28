from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=50)
    rollno=models.CharField(max_length=50)
    admno=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    parent=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    

    
