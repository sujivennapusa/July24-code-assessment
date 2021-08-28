from django.db import models
class Books(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    