from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_code=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    speciality=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.IntegerField()