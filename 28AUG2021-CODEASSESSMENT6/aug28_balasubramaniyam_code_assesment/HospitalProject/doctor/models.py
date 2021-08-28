from django.db import models

# Create your models here.
class Doctor(models.Model):
    doc_code=models.IntegerField()
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    specialisation=models.CharField(max_length=50)
    email=models.EmailField()