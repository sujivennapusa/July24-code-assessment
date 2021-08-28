from rest_framework import serializers
from books.models import Books
class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=("id","book_name","author","description","price","category")

