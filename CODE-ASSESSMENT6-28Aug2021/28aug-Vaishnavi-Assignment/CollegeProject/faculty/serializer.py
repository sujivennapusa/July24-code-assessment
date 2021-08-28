from django.db import models
from django.db.models import fields
from rest_framework import serializers
from faculty.models import Facultyapp

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model= Facultyapp
        fields = ('id','faculty_code', 'name', 'department', 'address', 'mobilenumber')

        