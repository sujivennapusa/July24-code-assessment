from django.db import models

# Create your models here.
class Studentapp(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    admno = models.IntegerField()
    college=models.CharField(max_length=50)
    parent_name=models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    department=models.CharField(max_length=20)
    
    