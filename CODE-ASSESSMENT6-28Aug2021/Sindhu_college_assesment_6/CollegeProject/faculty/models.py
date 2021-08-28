from django.db import models

# Create your models here.
class Faculty(models.Model):
    fcode=models.IntegerField()
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
