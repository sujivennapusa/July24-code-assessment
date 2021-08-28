from django.db import models

# Create your models here.
class Faculty(models.Model):
    facultycode=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)
  