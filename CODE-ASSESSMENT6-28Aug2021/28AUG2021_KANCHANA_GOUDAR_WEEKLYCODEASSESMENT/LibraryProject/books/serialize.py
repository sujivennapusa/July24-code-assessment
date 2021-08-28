from rest_framework import serializers
from books.models import Books

class BookSerialize(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=('id','Bname','Author','Des','Price','Category')