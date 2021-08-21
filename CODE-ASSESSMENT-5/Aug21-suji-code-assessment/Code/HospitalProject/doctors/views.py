from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from doctors.serializers import DoctorSerializer
from doctors.models import Doctor
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def doctor_add(request):
    if request.method=="POST":
        # getCode=request.POST.get("doctor_code")
        # getName=request.POST.get("name")
        # getAddress=request.POST.get("address")
        # getSpeciality=request.POST.get("speciality")
        # getUsername=request.POST.get("username")
        # getPassword=request.POST.get("password")
        # mydata={"doctor_code":getCode,"name":getName,"address":getAddress,"speciality":getSpeciality,"username":getUsername,"password":getPassword};
        # result=json.dumps(mydata)
        # return HttpResponse(result)
        mydata=JSONParser().parse(request)
        doctor_serialize=DoctorSerializer(data=mydata)
        if(doctor_serialize.is_valid()):
            doctor_serialize.save()
            return JsonResponse(doctor_serialize.data)
            return HttpResponse("Success")
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("No get method allowed")

@csrf_exempt
def doctor_list(request):
    if(request.method=="GET"):
        doctors=Doctor.objects.all()
        doctor_serializer=DoctorSerializer(doctors,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)      

@csrf_exempt
def doctor_details(request,fetchid):
    try:
        doctors=Doctor.objects.get(id=fetchid)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid Doctor Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        doctor_serialize=DoctorSerializer(doctors)
        return JsonResponse(doctor_serialize.data,safe=False,status=status.HTTP_200_OK)


    if(request.method=="DELETE"):
        doctors.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   

    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        doctor_serialize=DoctorSerializer(doctors,data=mydata)
        if(doctor_serialize.is_valid()):
            doctor_serialize.save()
            return JsonResponse(doctor_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(doctor_serialize.errors,status=status.HTTP_400_BAD_REQUEST)   
@csrf_exempt
def doctor_search(request,fetchdoctor_code):
    try:
        doctors=Doctor.objects.get(doctor_code=fetchdoctor_code)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid Doctor code",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        doctor_serialize=DoctorSerializer(doctors)
        return JsonResponse(doctor_serialize.data,safe=False,status=status.HTTP_200_OK)         

def register_interface(request):
    return render(request,'register.html') 
             
def login_interface(request):
    return render(request,'login.html')          