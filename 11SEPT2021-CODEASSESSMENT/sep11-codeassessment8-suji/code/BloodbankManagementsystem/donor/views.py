from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from donor.serializers import DonorSerializer
from donor.models import Donor
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.
@csrf_exempt
def donor_add(request):
    if request.method=="POST":
        # getName=request.POST.get("name")
        # getAddress=request.POST.get("address")
        # getBloodGroup=request.POST.get("bloodgroup")
        # getMobileNo=request.POST.get("mobileno")
        # getUsername=request.POST.get("username")
        # getPassword=request.POST.get("password")
        

        # mydict={"name":getName,"address":getAddress,"bloodgroup":getBloodGroup,"mobileno":getMobileNo,"username":getUsername,"password":getPassword};
        # result=json.dumps(mydict)
        # return HttpResponse(result)
        donordata=JSONParser().parse(request)
        donor_serialize=DonorSerializer(data=donordata)
        if(donor_serialize.is_valid()):
            donor_serialize.save()
            return redirect(logindonor)
            # return JsonResponse(donor_serialize.data)
            
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No get method allowed")


def logindonor(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')    

@csrf_exempt
def logincheck(request):
    try:
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")
        getDonors = Donor.objects.filter(username=getUsername, password=getPassword)
        user_serialiser = UserSerializer(getDonors, many=True)
        print(donor_serialiser.data)

            
    except Donor.DoesNotExist:
        return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")
    return HttpResponse("")    



    



   