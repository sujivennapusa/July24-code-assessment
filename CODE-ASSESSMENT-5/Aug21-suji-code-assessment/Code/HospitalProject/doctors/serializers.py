from django.db import models
from django.db.models import fields
from rest_framework import serializers
from doctors.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=('doctor_code','name','address','speciality','username','password')