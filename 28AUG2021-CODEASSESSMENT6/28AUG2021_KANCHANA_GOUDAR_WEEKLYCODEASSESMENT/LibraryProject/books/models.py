from django.db import models

# Create your models here.


# Create your models here.
class Books(models.Model):
    Bname=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Des=models.CharField(max_length=50)
    Price=models.CharField(max_length=50)
    Category=models.CharField(max_length=50)