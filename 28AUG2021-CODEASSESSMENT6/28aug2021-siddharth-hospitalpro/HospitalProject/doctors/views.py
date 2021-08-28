from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer



@csrf_exempt
def addDoctor(request):
    if(request.method=="POST"):
        
        dserialize=DoctorSerializer(data=request.POST)
        if (dserialize.is_valid()):
            dserialize.save() 
            return response.JsonResponse(dserialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization")

def register(request):
    return render(request,'registere.html')


@csrf_exempt
def viewDoctor(request):
    if (request.method=='GET'):
        d1=Doctor.objects.all()
        dserial=DoctorSerializer(d1,many=True)
        return response.JsonResponse(dserial.data, safe=False)

def Doctorview(request):
    fetch=requests.get("http://127.0.0.1:8000/doctors/viewdoctors/").json()
    return render(request,'viewdoctor.html',{"data":fetch})

@csrf_exempt
def viewDoctordetails(request,id):
    try:
        d1=Doctor.objects.get(id=id)
        if (request.method=='GET'):
            dserial=DoctorSerializer(d1) 
            return response.JsonResponse(dserial.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            d1.delete()
            return HttpResponse("Doctor is deleted")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            dserial=DoctorSerializer(d1,data=mydata)
            if (dserial.is_valid()):
                dserial.save()
                return response.JsonResponse(dserial.data,status=status.HTTP_200_OK)
    except Doctor.DoesNotExist:
        return HttpResponse("invalid ID ")


@csrf_exempt
def searchapi(request):
    try:
        getdcode=request.POST.get("dcode")
        getdet=Doctor.objects.filter(dcode=getdcode)
        dserial=DoctorSerializer(getdet,many=True)
        return render(request,"searche.html",{"data":dserial.data})
    except Doctor.DoesNotExist:
        return HttpResponse("invalid Doctor code")
    except:
        return HttpResponse("something went wrong")

def searchdoctor(request):
    return render(request,'searche.html')



@csrf_exempt
def updatesearchapi(request):
    try:
        getdcode=request.POST.get("dcode")
        getdet=Doctor.objects.filter(dcode=getdcode)
        dserial=DoctorSerializer(getdet,many=True)
        return render(request,"updatee.html",{"data":dserial.data})
    except Doctor.DoesNotExist:
        return HttpResponse("invalid Doctor code")
    except:
        return HttpResponse("something went wrong")

    
    
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getnewdcode=request.POST.get('newdcode')
        getnewdname=request.POST.get('newdname')
        getnewdaddress=request.POST.get('newdaddress')
        getnewdmobile=request.POST.get('newdmobile')
        getnewdspecial=request.POST.get('newdspecial')
        getnewdemail=request.POST.get('newdemail')
        
    
        mydata={"dcode":getnewdcode,"dname":getnewdname,"daddress":getnewdaddress,"dmobile":getnewdmobile,"dspecial":getnewdspecial,"demail":getnewdemail}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/doctors/viewdoctordetails/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updated successfully")

def update(request):
    return render(request,'updatee.html')



@csrf_exempt
def deletesearchapi(request):
    try:
        getdcode=request.POST.get("dcode")
        getdet=Doctor.objects.filter(dcode=getdcode)
        dserial=DoctorSerializer(getdet,many=True)
        return render(request,"deletee.html",{"data":dserial.data})
    except Doctor.DoesNotExist:
        return HttpResponse("invalid Doctor code")
    except:
        return HttpResponse("something went wrong")
    

@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        
        ApiLink="http://localhost:8000/doctors/viewdoctordetails/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")

def delete(request):
    return render(request,'deletee.html')




