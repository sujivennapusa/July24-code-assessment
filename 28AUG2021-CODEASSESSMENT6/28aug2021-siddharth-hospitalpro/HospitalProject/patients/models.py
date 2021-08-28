from django.db import models


class Patient(models.Model):
    pcode=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)
    paddress=models.CharField(max_length=50)
    pemail=models.CharField(max_length=50)
    pphone=models.CharField(max_length=50)
    ppincode=models.CharField(max_length=50)
    
