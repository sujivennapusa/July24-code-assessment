from requests.sessions import Request
import json
from django.shortcuts import redirect, render
from patient.models import Patient
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from patient.serializers import PatientSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.


def myPatient(request):
    return render(request,'patient.html')

def myWelcomePage(request):
    return render(request,'welcome.html')


def myViewAllPage(request):
    fetchdata=requests.get("http://127.0.0.1:8000/patient/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})

@csrf_exempt
def myPatientDetails(request,id):
    try:
        patients=Patient.objects.get(id=id)
        if (request.method=="GET"):    
            patient_serializer=PatientSerializer(patients)
            return JsonResponse(patient_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            patients.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            patient_serialize=PatientSerializer(patients,data=dict)
            if(patient_serialize.is_valid()):
                patient_serialize.save()
                return JsonResponse(patient_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(patient_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


def mySearch(request):
    return render(request,'search.html')

def myUpdate(request):
    return render(request,'update.html')


def myDelete(request):
    return render(request,'delete.html')


@csrf_exempt
def UpdateRead(request):
    getNewId=request.POST.get("newid")
    getNewPatcode=request.POST.get("newpatcode")
    getNewname=request.POST.get("newname")
    getNewaddress=request.POST.get("newaddress")
    getNewemail=request.POST.get("newemail")
    getNewphone=request.POST.get("newphone")
    getNewpincode=request.POST.get("newpincode")
    mydata={'pat_code':getNewPatcode,'name':getNewname,'address':getNewaddress,'email':getNewemail,'phone':getNewphone,'pincode':getNewpincode}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/patient/viewpatient/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myViewAllPage)
    

@csrf_exempt
def UpdateSearchAPI(request):
    try:
        getPat_code=request.POST.get("pat_code")
        getName=Patient.objects.filter(pat_code=getPat_code)
        patient_serializer=PatientSerializer(getName,many=True)
        return render(request,"update.html",{"data":patient_serializer.data})
        #return JsonResponse(patient_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


# Create your views here.
@csrf_exempt
def DeleteRead(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/patient/viewpatient/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllPage)

@csrf_exempt
def DeleteSearchAPI(request):
    try:
        getPat_code=request.POST.get("pat_code")
        getName=Patient.objects.filter(pat_code=getPat_code)
        patient_serializer=PatientSerializer(getName,many=True)
        return render(request,"delete.html",{"data":patient_serializer.data})
        #return JsonResponse(patient_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def SearchAPI(request):
    try:
        getPat_code=request.POST.get("pat_code")
        getName=Patient.objects.filter(pat_code=getPat_code)
        patient_serializer=PatientSerializer(getName,many=True)
        return render(request,"search.html",{"data":patient_serializer.data})
        #return JsonResponse(patient_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")


@csrf_exempt
def myPatientList(request):
    if(request.method=="GET"):
        patients=Patient.objects.all()
        patient_serializer=PatientSerializer(patients,many=True)
        return JsonResponse(patient_serializer.data,safe=False)

@csrf_exempt
def myPatientPage(request):
    if(request.method=="POST"):
        # dict=JSONParser().parse(request)
        patient_serialize=PatientSerializer(data=request.POST)
        if(patient_serialize.is_valid()):
            patient_serialize.save()
            return redirect(myViewAllPage)
            #return JsonResponse(patient_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        