from django.db import models

class Faculty(models.Model):
    fcode = models.IntegerField()
    dept = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobno = models.BigIntegerField()
    