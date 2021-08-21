from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_code=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    disease=models.CharField(max_length=50)
    admitstatus=models.BooleanField()
    