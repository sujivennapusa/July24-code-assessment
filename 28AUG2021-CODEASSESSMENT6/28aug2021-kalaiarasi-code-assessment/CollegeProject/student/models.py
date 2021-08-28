from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    adminno=models.IntegerField()
    college=models.CharField(max_length=50)
    parent=models.CharField(max_length=50)
    mobnum=models.BigIntegerField()
    department=models.CharField(max_length=50)
    