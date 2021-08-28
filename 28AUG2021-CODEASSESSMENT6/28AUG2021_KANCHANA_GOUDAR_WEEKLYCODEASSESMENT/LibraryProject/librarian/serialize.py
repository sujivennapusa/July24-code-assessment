from rest_framework import serializers
from librarian.models import Librarian

class LibrarianSerialize(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields=('id','Lcode','Name','Address','Mobile','Pincode','Email')