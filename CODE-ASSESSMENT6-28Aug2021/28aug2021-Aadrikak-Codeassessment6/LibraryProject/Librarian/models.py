from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Librarian(models.Model):
    lcode=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    ladd=models.CharField(max_length=50)
    lmob=models.CharField(max_length=50)
    lpincode=models.CharField(max_length=50)
    lemail=models.CharField(max_length=50)