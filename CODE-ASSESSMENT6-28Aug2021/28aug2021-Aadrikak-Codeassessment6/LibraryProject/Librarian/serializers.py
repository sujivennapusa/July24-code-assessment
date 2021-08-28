from rest_framework import serializers
from Librarian.models import Librarian, Librarian

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields=('id','lcode','lname','ladd','lmob','lpincode','lemail')


    

