from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    admno=models.IntegerField()
    rollno=models.IntegerField()
    college=models.CharField(max_length=50)
    parentname=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()
    dept=models.CharField(max_length=50)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    