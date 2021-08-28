from re import search
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import requests
from patients.models import Hospital
from patients.serializers import hospitalSerializer
from rest_framework import status
import json

# Create your views here.

def mainpage(request):
    return render(request,'main.html')

def home(request):
    return render(request,'home.html')

def search_c(request):
    return render(request,'search.html')

def update(request):
    return render(request,'update.html')


def delete(request):
    return render(request,'delete.html')


def add_customer(request):
    return render(request,'add.html')

def view_customer(request):
    x=requests.get("http://127.0.0.1:8000/patient/viewall/").json()
    return render(request,'view.html',{"data":x})




@csrf_exempt
def addcustomer(request):
    if(request.method=="POST"):
        # mydit=JSONParser().parse(request)
        h_serial=hospitalSerializer(data=request.POST)
        if (h_serial.is_valid()):
            h_serial.save()
            return JsonResponse(h_serial.data,status=status.HTTP_200_OK)
    
        else:
            return HttpResponse("error in serilazation",status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("ERROR",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewcustomer(request):
    if(request.method=="GET"):
        c1=Hospital.objects.all()
        h_serial=hospitalSerializer(c1,many=True)
        return JsonResponse(h_serial.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def update_d(request,fetchid):
    try:
        c1=Hospital.objects.get(id=fetchid)
        if(request.method=="GET"):
            h_serial=hospitalSerializer(c1)
            return JsonResponse(h_serial.data,safe=False,status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            mydit=JSONParser().parse(request)
            h_serial=hospitalSerializer(c1,data=mydit)
            if (h_serial.is_valid()):
                h_serial.save()
                return JsonResponse(h_serial.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(h_serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    except Hospital.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)      



@csrf_exempt
def search_customer(request):
    try:
        getname=request.POST.get("patient_code")
        print(getname)
        getcustomer=Hospital.objects.filter(patient_code=getname)
        h_serial=hospitalSerializer(getcustomer,many=True)
        return render(request,"search.html",{"data":h_serial.data})

        # return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)

    except Hospital.DoesNotExist:
        return HttpResonse("Invalid customer name",status=status.HTTP_404_NOT_FOUND)
    except: 
        return HttpResponse("something went wrong",status=status.HTTP_404_NOT_FOUND)   

@csrf_exempt
def update_api(request):
    try:
        getna=request.POST.get("patient_code")
        print(getna)
        getdata=Hospital.objects.filter(patient_code=getna)
        h_serial=hospitalSerializer(getdata,many=True)
        return render(request,"update.html",{"data":h_serial.data})

    except Hospital.DoesNotExist:
        return HttpResonse("Invalid name",status=status.HTTP_404_NOT_FOUND)

    except: 
        return HttpResponse("error",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data(request):
    getid=request.POST.get("newid")

    getname=request.POST.get("newname")
    getemail=request.POST.get("newemail")
    getadress=request.POST.get("newaddress")
    getphno=request.POST.get("newphone")
    getpincode=request.POST.get("newpincode")
    getp=request.POST.get("newpatient_code")


    mydata={'name':getname,'email':getemail,'address':getadress,'phone':getphno,'pincode':getpincode,'id':getid,'patient_code':getp}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/patient/view/" + getid
    requests.put(Apilink, data=jsondata)
    return HttpResponse("data has updated sucessfuly")




@csrf_exempt
def deleteapi(request):
    try:
        getbno=request.POST.get("patient_code")
        getc=Hospital.objects.filter(patient_code=getbno)
        h_serial=hospitalSerializer(getc,many=True)
        return render(request,"delete.html",{"data":h_serial.data})
        # return JsonResponse(h_serial.data,safe=False,status=status.HTTP_200_OK)
    except Hospital.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def delete_data(request):
    getid=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/patient/view/"+getid
    requests.delete(Apilink)
    return HttpResponse("data has deleted sucessfully")
