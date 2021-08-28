from rest_framework import serializers
from student.models import College
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=College
        fields=("id","name","admnno","rollno","college","parentname","mobilenumber","department1")
