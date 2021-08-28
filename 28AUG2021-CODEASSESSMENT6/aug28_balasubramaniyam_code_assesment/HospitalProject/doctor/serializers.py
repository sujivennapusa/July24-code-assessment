from rest_framework import serializers
from doctor.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=('id','doc_code','name','address','mobile','specialisation','email')
        