from django.db import models

# Create your models here.
class Patient(models.Model):
    pat_code=models.IntegerField()
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    pincode=models.IntegerField()
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)