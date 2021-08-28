from django.db import models
class Librarian(models.Model):
    librarian_code=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    pincode=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    
