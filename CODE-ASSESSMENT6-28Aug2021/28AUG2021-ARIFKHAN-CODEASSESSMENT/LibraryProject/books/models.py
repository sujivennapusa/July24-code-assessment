from django.db import models
class Book(models.Model):
    bookname=models.CharField(max_length=50)
    author=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    price=models.CharField(max_length=25)
    category=models.CharField(max_length=50)
    
