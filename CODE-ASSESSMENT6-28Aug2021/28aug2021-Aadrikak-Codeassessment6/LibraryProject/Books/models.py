from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Book(models.Model):
    bname=models.CharField(max_length=50)
    bauthor=models.CharField(max_length=50)
    bdescp=models.CharField(max_length=100)
    bprice=models.CharField(max_length=50)
    bcategory=models.CharField(max_length=50)
    
   
    

