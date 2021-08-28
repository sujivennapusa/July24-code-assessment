from django.db import models

# Create your models here.
class Facultyapp(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True,serialize=False)
    faculty_code=models.IntegerField()
    name = models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    mobilenumber=models.BigIntegerField()
    
    
    