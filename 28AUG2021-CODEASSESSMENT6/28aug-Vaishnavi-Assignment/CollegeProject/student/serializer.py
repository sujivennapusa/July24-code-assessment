from django.db import models
from django.db.models import fields
from rest_framework import serializers
from student.models import Studentapp

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Studentapp
        fields = ('id','name','rollno','admno','college','parent_name','mobile','department')

        
  
    
