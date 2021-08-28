from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from Librarian.models import Librarian
from Librarian.serializers import LibrarianSerializer

@csrf_exempt
def addLibrarian(request):
    if(request.method=="POST"):
        
        libserial=LibrarianSerializer(data=request.POST)
        if (libserial.is_valid()):
            libserial.save() 
            return response.JsonResponse(libserial.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization")

def register(request):
    return render(request,'registeration.html')



@csrf_exempt
def viewLibrarian(request):
    if (request.method=='GET'):
        lib=Librarian.objects.all()
        libserial=LibrarianSerializer(lib,many=True)
        return response.JsonResponse(libserial.data, safe=False)

def Librarianview(request):
    fetch=requests.get("http://127.0.0.1:8000/librarians/viewlibrarian/").json()
    return render(request,'viewlib.html',{"data":fetch})


@csrf_exempt
def viewLibdetails(request,id):
    try:
        lib=Librarian.objects.get(id=id)
        if (request.method=='GET'):
            libserial=LibrarianSerializer(lib) 
            return response.JsonResponse(libserial.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            lib.delete()
            return HttpResponse("Librarian is deleted")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            libserial=LibrarianSerializer(lib,data=mydata)
            if (libserial.is_valid()):
                libserial.save()
                return response.JsonResponse(libserial.data,status=status.HTTP_200_OK)
    except Librarian.DoesNotExist:
        return HttpResponse("invalid ID ")


@csrf_exempt
def searchapi(request):
    try:
        getlcode=request.POST.get("lcode")
        getdet=Librarian.objects.filter(lcode=getlcode)
        libserial=LibrarianSerializer(getdet,many=True)
        return render(request,"searching.html",{"data":libserial.data})
    except Librarian.DoesNotExist:
        return HttpResponse("invalid Librarian code")
    except:
        return HttpResponse("something went wrong")

def searchemp(request):
    return render(request,'searching.html')


@csrf_exempt
def updatesearchapi(request):
    try:
        getlcode=request.POST.get("lcode")
        getdet=Librarian.objects.filter(lcode=getlcode)
        libserial=LibrarianSerializer(getdet,many=True)
        return render(request,"updating.html",{"data":libserial.data})
    except Librarian.DoesNotExist:
        return HttpResponse("invalid Librarian Code")
    except:
        return HttpResponse("something went wrong")
    
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getnewlcode=request.POST.get('newlcode')
        getnewlname=request.POST.get('newlname')
        getnewladd=request.POST.get('newladd')
        getnewlmob=request.POST.get('newlmob')
        getnewlpincode=request.POST.get('newlpincode')
        getnewlemail=request.POST.get('newlemail')
      
        
    
        mydata={"lcode":getnewlcode,"lname":getnewlname,"ladd":getnewladd,"lmob":getnewlmob,"lpincode":getnewlpincode,"lemail":getnewlemail}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/librarians/viewLibrariandetails/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updated successfully")

def update(request):
    return render(request,'updating.html')



@csrf_exempt
def deletesearchapi(request):
    try:
        getlcode=request.POST.get("lcode")
        getdet=Librarian.objects.filter(lcode=getlcode)
        libserial=LibrarianSerializer(getdet,many=True)
        return render(request,"deleting.html",{"data":libserial.data})
    except Librarian.DoesNotExist:
        return HttpResponse("invalid Librarians code")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/librarians/viewLibrariandetails/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")

def delete(request):
    return render(request,'deleting.html')



