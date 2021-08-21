from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from patients.serializers import PatientSerializer
from patients.models import Patient
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def patient_add(request):
    if request.method=="POST":
        # getCode=request.POST.get("patient_code")
        # getName=request.POST.get("name")
        # getAddress=request.POST.get("address")
        # getDisease=request.POST.get("disease")
        # getAdmitstatus=request.POST.get("admitstatus")
        # mydata={"patient_code":getCode,"name":getName,"address":getAddress,"disease":getDisease,"admitstatus":getAdmitstatus};
        # result=json.dumps(mydata)
        # return HttpResponse(result)
        mydata=JSONParser().parse(request)
        patient_serialize=PatientSerializer(data=mydata)
        if(patient_serialize.is_valid()):
            patient_serialize.save()
            return JsonResponse(patient_serialize.data)
            return HttpResponse("Success")
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("No get method allowed")
    
    
    

@csrf_exempt
def patient_list(request):
    if(request.method=="GET"):
        patients=Patient.objects.all()
        patient_serializer=PatientSerializer(patients,many=True)
        return JsonResponse(patient_serializer.data,safe=False)

@csrf_exempt
def patient_details(request,fetchid):
    try:
        patients=Patient.objects.get(id=fetchid)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid Patient Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        patient_serialize=PatientSerializer(patients)
        return JsonResponse(patient_serialize.data,safe=False,status=status.HTTP_200_OK)


    if(request.method=="DELETE"):
        patients.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   

    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        patient_serialize=PatientSerializer(patients,data=mydata)
        if(patient_serialize.is_valid()):
            patient_serialize.save()
            return JsonResponse(patient_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(patient_serialize.errors,status=status.HTTP_400_BAD_REQUEST)   
@csrf_exempt
def patient_search(request,fetchpatient_code):
    try:
        patients=Patient.objects.get(patient_code=fetchpatient_code)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid Patient code",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        patient_serialize=PatientSerializer(patients)
        return JsonResponse(patient_serialize.data,safe=False,status=status.HTTP_200_OK)         

def patient_interface(request):
    return render(request,'patient.html')