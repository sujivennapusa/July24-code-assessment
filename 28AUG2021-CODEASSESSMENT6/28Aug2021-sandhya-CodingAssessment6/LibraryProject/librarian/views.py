from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from librarian.serializers import librarianSerializer
from librarian.models import Librarian
from rest_framework.parsers import JSONParser 
from rest_framework import status
import requests
@csrf_exempt
def searchapi(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getLibrarian=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serializer=librarianSerializer(getLibrarian,many=True)
        return render(request,"searchlib.html",{"data":librarian_serializer.data})

    except:
        return HttpResponse("invalid Librarian Code")
@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    getlibrariancode=request.POST.get("newlibrariancode")
    getname=request.POST.get("newname")
    getaddress=request.POST.get("newaddress")
    getmobile=request.POST.get("newmobile")
    getpincode=request.POST.get("newpincode")
    getemailid=request.POST.get("newemailid")
    mydata={"librarian_code":getlibrariancode,"name":getname,"address":getaddress,"mobile":getmobile,"pincode":getpincode,"emailid":getemailid}
    jsondata=json.dumps(mydata)
    ApiLink="http://localhost:8000/librarian/view/"+ getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("data updated successfully")
@csrf_exempt 
def update_api(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getLibrarian=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serializer=librarianSerializer(getLibrarian,many=True)
        return render(request,"updatelib.html",{"data":librarian_serializer.data})

    except:
        return HttpResponse("invalid Library Code")
@csrf_exempt
def delete_data_read(request):
    getId=request.POST.get("newid")
    ApiLink="http://localhost:8000/librarian/view/"+ getId 
    requests.delete(ApiLink)
    return HttpResponse("data deleted successfully")
@csrf_exempt
def delete_api(request):
    try:
        getlibrariancode=request.POST.get("librarian_code")
        getLibrarian=Librarian.objects.filter(librarian_code=getlibrariancode)
        librarian_serializer=librarianSerializer(getLibrarian,many=True)
        return render(request,"deletelib.html",{"data":librarian_serializer.data})
    except:
        return HttpResponse("invalid librarian_code ")
@csrf_exempt
def librarianPage(request):
    if(request.method=="POST"):
    #    mydict=JSONParser().parse(request)   
       librarian_serialize=librarianSerializer(data=request.POST)  
       if(librarian_serialize.is_valid()):
           librarian_serialize.save()
           return redirect(viewall)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
@csrf_exempt
def librarian_list(request):
    if(request.method=="GET"):
        librarian=Librarian.objects.all()
        librarian_serializer=librarianSerializer(librarian,many=True)
        return JsonResponse(librarian_serializer.data,safe=False)
@csrf_exempt
def librarian_details(request,fetchid):
    try:
        librarian=Librarian.objects.get(id=fetchid)
        if(request.method=="GET"):
            librarian_serializer=librarianSerializer(librarian)
            return JsonResponse(librarian_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            librarian.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            librarian_serializer=librarianSerializer(librarian,data=mydict)
            if(librarian_serializer.is_valid()):
                librarian_serializer.save()
                return JsonResponse(librarian_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(librarian_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except librarian.DoesNotExist:
        return HttpResponse("invalid librarian id",status=status.HTTP_404_NOT_FOUND)

def register(request):
    return render(request,'librarianregister.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/librarian/viewall/").json()
    return render(request,'viewalllib.html',{"data":fetchdata})
def search_view(request):
    return render(request,'searchlib.html')
def update_view(request):
    return render(request,'updatelib.html')
def delete_view(request):
    return render(request,'deletelib.html')