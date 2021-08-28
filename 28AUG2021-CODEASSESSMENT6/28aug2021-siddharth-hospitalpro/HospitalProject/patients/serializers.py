from rest_framework import serializers
from patients.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=('id','pcode','pname','paddress','pemail','pphone','ppincode')