from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from librarian.models import Librarian
from librarian.serializers import LibrarianSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

@csrf_exempt
def addlibrarian(request):
    if (request.method=="POST"):
        getlibrarain=int(request.POST.get('librariancode'))
        getname=request.POST.get('name')
        getaddress=request.POST.get('address')
        getmobilenumber=int(request.POST.get('mobileno'))
        getpincode=request.POST.get('pincode')
        getemail=request.POST.get('email')
    
        mydata={'librariancode':getlibrarain,'name':getname,'address':getaddress,'mobileno':getmobilenumber,'pincode':getpincode,'email':getemail}

        # mydata=JSONParser().parse(request)
        librarain_serialize=LibrarianSerializer(data=mydata)
        
        if (librarain_serialize.is_valid()):
            librarain_serialize.save()
            return redirect(librarianviewss)
            # return JsonResponse(librarain_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def librarian_all(request):
    if(request.method=="GET"):
        k=Librarian.objects.all()
        librarain_serializer=LibrarianSerializer(k,many=True)
        return JsonResponse(librarain_serializer.data,safe=False)

@csrf_exempt
def librarian_single(request,fetchid):
    
    sh=Librarian.objects.get(id=fetchid)

    
    if(request.method=="GET"):
        librarain_serialize=LibrarianSerializer(sh)
        return JsonResponse(librarain_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        librarain_serialize=LibrarianSerializer(sh,data=mydata)

        if(librarain_serialize.is_valid()):
            librarain_serialize.save()
            return JsonResponse(librarain_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(librarain_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

def registerlibrarian(request):
    return render(request,'register.html')

def librarianviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/librarian/viewall/").json
    return render(request,'view.html',{"data":fetchdata})

def librariansearch(request):
    return render(request,'search.html')

def librarianupdate(request):
    return render(request,'update.html')

@csrf_exempt
def searchapi(request):
    try:
        getlibrariancode=request.POST.get("librariancode")
        getlib=Librarian.objects.filter(librariancode=getlibrariancode)
        librarian_serializer=LibrarianSerializer(getlib,many=True)
        
        return render(request,"search.html",{"data":librarian_serializer.data})
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid librariancode")
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def updatesearchapi(request):
    try:
        getlibrariancode=request.POST.get("librariancode")
        getlib=Librarian.objects.filter(librariancode=getlibrariancode)
        librarian_serializer=LibrarianSerializer(getlib,many=True)

        return render(request,"update.html",{"data":librarian_serializer.data})
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid librariancode")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getlibrariancode=request.POST.get('newlibrariancode')
        getname=request.POST.get('newname')
        getaddress=request.POST.get('newaddress')
        getmobilenumber=int(request.POST.get('newmobileno'))
        getpincode=request.POST.get("newpincode")
        getemail=request.POST.get("newemail")
        
        mydata={'librariancode':getlibrariancode,'name':getname,'address':getaddress,'mobileno':getmobilenumber,'pincode':getpincode,'email':getemail}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/librarian/view/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

def librariandelete(request):
    return render(request,'delete.html')

@csrf_exempt
def deletesearchapi(request):
    try:
        getlibrariancode=request.POST.get("librariancode")
        getlib=Librarian.objects.filter(librariancode=getlibrariancode)
        librarian_serializer=LibrarianSerializer(getlib,many=True)
        return render(request,"delete.html",{"data":librarian_serializer.data})
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid librariancode")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/librarian/view/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")