from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    admno = models.IntegerField()
    college = models.CharField(max_length=50)
    parent = models.CharField(max_length=50)
    mobno = models.BigIntegerField()
    dept = models.CharField(max_length=50)
