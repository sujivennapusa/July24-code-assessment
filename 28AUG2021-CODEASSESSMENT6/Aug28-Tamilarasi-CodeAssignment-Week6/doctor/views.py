from requests.sessions import Request
import json
from django.shortcuts import redirect, render
from doctor.models import Doctor
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from doctor.serializers import DoctorSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.


def myDoctor(request):
    return render(request,'doctor.html')

def myWelcomeDoctorPage(request):
    return render(request,'welcome1.html')


def myViewAllPage1(request):
    fetchdata=requests.get("http://127.0.0.1:8000/doctor/viewall1/").json()
    return render(request,'viewall1.html',{"data":fetchdata})

@csrf_exempt
def myDoctorDetails(request,id):
    try:
        doctors=Doctor.objects.get(id=id)
        if (request.method=="GET"):    
            doctor_serializer=DoctorSerializer(doctors)
            return JsonResponse(doctor_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            doctors.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            doctor_serialize=DoctorSerializer(doctors,data=dict)
            if(doctor_serialize.is_valid()):
                doctor_serialize.save()
                return JsonResponse(doctor_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(doctor_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


def mySearch1(request):
    return render(request,'search1.html')

def myUpdate1(request):
    return render(request,'update1.html')


def myDelete1(request):
    return render(request,'delete1.html')


@csrf_exempt
def UpdateRead1(request):
    getNewId=request.POST.get("newid")
    getNewDoccode=request.POST.get("newdoccode")
    getNewname=request.POST.get("newname")
    getNewaddress=request.POST.get("newaddress")
    getNewmobile=request.POST.get("newmobile")
    getNewspecialisation=request.POST.get("newspecialisation")
    getNewemail=request.POST.get("newemail")
    mydata={'doc_code':getNewDoccode,'name':getNewname,'address':getNewaddress,'mobile':getNewmobile,'specialisation':getNewspecialisation,'email':getNewemail}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/doctor/viewdoctor1/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myViewAllPage1)
    

@csrf_exempt
def UpdateSearchAPI1(request):
    try:
        getDoc_code=request.POST.get("doc_code")
        getName=Doctor.objects.filter(doc_code=getDoc_code)
        doctor_serializer=DoctorSerializer(getName,many=True)
        return render(request,"update1.html",{"data":doctor_serializer.data})
        #return JsonResponse(doctor_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


# Create your views here.
@csrf_exempt
def DeleteRead1(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/doctor/viewdoctor1/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllPage1)

@csrf_exempt
def DeleteSearchAPI1(request):
    try:
        getDoc_code=request.POST.get("doc_code")
        getName=Doctor.objects.filter(doc_code=getDoc_code)
        doctor_serializer=DoctorSerializer(getName,many=True)
        return render(request,"delete1.html",{"data":doctor_serializer.data})
        #return JsonResponse(doctor_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def SearchAPI1(request):
    try:
        getDoc_code=request.POST.get("doc_code")
        getName=Doctor.objects.filter(doc_code=getDoc_code)
        doctor_serializer=DoctorSerializer(getName,many=True)
        return render(request,"search1.html",{"data":doctor_serializer.data})
        #return JsonResponse(doctor_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")


@csrf_exempt
def myDoctorList(request):
    if(request.method=="GET"):
        doctors=Doctor.objects.all()
        doctor_serializer=DoctorSerializer(doctors,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)

@csrf_exempt
def myDoctorPage(request):
    if(request.method=="POST"):
        # dict=JSONParser().parse(request)
        doctor_serialize=DoctorSerializer(data=request.POST)
        if(doctor_serialize.is_valid()):
            doctor_serialize.save()
            return redirect(myViewAllPage1)
            #return JsonResponse(doctor_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)