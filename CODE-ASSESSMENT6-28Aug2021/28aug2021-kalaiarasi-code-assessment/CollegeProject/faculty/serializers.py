from rest_framework import serializers
from faculty.models import Faculty

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=('id','name','fcode','address','mobnum','department')