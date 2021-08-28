from django.shortcuts import render
from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from patients.serializers import PatientSerializer
from patients.models import Patient
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

@csrf_exempt
def addPatient(request):
    if(request.method=="POST"):
        pserial=PatientSerializer(data=request.POST)
        if (pserial.is_valid()):
            pserial.save() 
            return response.JsonResponse(pserial.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization")
    
def register(request):
    return render(request,'register.html')


@csrf_exempt
def viewPatient(request):
    if (request.method=='GET'):
        p1=Patient.objects.all()
        pserial=PatientSerializer(p1,many=True)
        return response.JsonResponse(pserial.data, safe=False)

def Patientview(request):
    fetch=requests.get("http://127.0.0.1:8000/patients/viewpatient/").json()
    return render(request,'viewpatient.html',{"data":fetch})


@csrf_exempt
def viewPatientdetails(request,id):
    try:
        p1=Patient.objects.get(id=id)
        if (request.method=='GET'):
            pserial=PatientSerializer(p1) 
            return response.JsonResponse(pserial.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            p1.delete()
            return HttpResponse("Patient Deleted")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            pserial=PatientSerializer(p1,data=mydata)
            if (pserial.is_valid()):
                pserial.save()
                return response.JsonResponse(pserial.data,status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return HttpResponse("invalid ID ")




@csrf_exempt
def searchapi(request):
    try:
        getp=request.POST.get("pcode")
        getpat=Patient.objects.filter(pcode=getp)
        pserial=PatientSerializer(getpat,many=True)
        return render(request,"search.html",{"data":pserial.data})
    except Patient.DoesNotExist:
        return HttpResponse("invalid Patient Code")
    except:
        return HttpResponse("Something Went wrong")


def searchpatient(request):
    return render(request,'search.html')





@csrf_exempt
def updatesearchapi(request):
    try:
        getp=request.POST.get("pcode")
        getpat=Patient.objects.filter(pcode=getp)
        pserial=PatientSerializer(getpat,many=True)
        return render(request,"update.html",{"data":pserial.data})
    except Patient.DoesNotExist:
        return HttpResponse("invalid Patient Code")
    except:
        return HttpResponse("Something Went wrong")

    

@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getnewpcode=request.POST.get('newpcode')
        getnewpname=request.POST.get('newpname')
        getnewpaddress=request.POST.get('newpaddress')
        getnewpemail=request.POST.get('newpemail')
        getnewpphone=int(request.POST.get('newpphone'))
        getnewppincode=request.POST.get('newppincode')
        
    
        mydata={"pcode":getnewpcode,"pname":getnewpname,"paddress":getnewpaddress,"pemail":getnewpemail,"pphone":getnewpphone,"ppincode":getnewppincode}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/patients/viewpatientdetails/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

def update(request):
    return render(request,'update.html')





@csrf_exempt
def deletesearchapi(request):
    try:
        getp=request.POST.get("pcode")
        getpat=Patient.objects.filter(pcode=getp)
        pserial=PatientSerializer(getpat,many=True)
        return render(request,"delete.html",{"data":pserial.data})
    except Patient.DoesNotExist:
        return HttpResponse("invalid Patient Code")
    except:
        return HttpResponse("Something Went wrong")
    
@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/patients/viewpatientdetails/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")


def delete(request):
    return render(request,'delete.html')


