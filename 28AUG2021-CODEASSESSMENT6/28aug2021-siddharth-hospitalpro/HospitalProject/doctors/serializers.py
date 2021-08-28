from rest_framework import serializers
from doctors.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=('id','dcode','dname','daddress','dmobile','dspecial','demail')

