from django.db import models

# Create your models here.
class Librarian(models.Model):
    Lcode=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)