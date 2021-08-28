from django.db import models
from django.db.models import fields
from rest_framework import serializers
from faculty.models import Faculty

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=('id','facultycode','department','fname','address','mobileno')