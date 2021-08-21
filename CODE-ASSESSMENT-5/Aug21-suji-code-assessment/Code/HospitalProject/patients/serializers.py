from django.db import models
from django.db.models import fields
from rest_framework import serializers
from patients.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=('patient_code','name','address','disease','admitstatus')