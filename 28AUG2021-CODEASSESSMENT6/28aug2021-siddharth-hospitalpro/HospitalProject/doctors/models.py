from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Doctor(models.Model):
    dcode=models.CharField(max_length=50)
    dname=models.CharField(max_length=50)
    daddress=models.CharField(max_length=50)
    dmobile=models.CharField(max_length=50)
    dspecial=models.CharField(max_length=50)
    demail=models.CharField(max_length=50)
