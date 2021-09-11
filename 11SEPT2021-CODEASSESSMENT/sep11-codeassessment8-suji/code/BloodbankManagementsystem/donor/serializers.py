from django.db import models
from django.db.models import fields
from rest_framework import serializers
from donor.models import Donor,Blogs

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('name','address','bloodgroup','mobileno','username','password')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields=('donorid','donordata')
