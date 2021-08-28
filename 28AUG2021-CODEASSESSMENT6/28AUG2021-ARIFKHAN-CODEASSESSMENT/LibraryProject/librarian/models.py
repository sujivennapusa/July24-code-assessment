from django.db import models
class Librarian(models.Model):
    librariancode=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=25)
    mobileno=models.BigIntegerField()
    pincode=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    