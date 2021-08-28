from rest_framework import serializers
from librarian.models import Librarian
class librarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields=("id","librarian_code","name","address","mobile","pincode","emailid")

