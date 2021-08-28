from rest_framework import serializers
from librarian.models import Librarian
class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields=("id","librariancode","name","address","mobileno","pincode","email")