from django.db import models

# Create your models here.
class Faculty(models.Model):
    name=models.CharField(max_length=50)
    fcode=models.IntegerField()
    address=models.CharField(max_length=50)
    mobnum=models.BigIntegerField()
    department=models.CharField(max_length=50)
    