from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from librarian.models import Librarian
from librarian.serialize import LibrarianSerialize
def Addlibrarian(request):
    return render(request,'Add.html')
def Viewalllibrarian(request):
    fetchdata=requests.get("http://127.0.0.1:8000/librarian/viewallapi/").json()
    return render(request,'views.html',{"data":fetchdata})
def Searchlibrarian(request):
    return render(request,'search.html')
def Updatelibrarian(request):
    return render(request,'update.html')
def Deletelibrarian(request):
    return render(request,'delete.html')


@csrf_exempt
def Librarianadd(request):
    if (request.method=="POST"):
        lib_s=LibrarianSerialize(data=request.POST)
        if(lib_s.is_valid()):
            lib_s.save()
            # return JsonResponse(lib_s.data)
            return redirect(Viewalllibrarian)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No get method is allowed")
def Librarianviewall(request):
    if (request.method=="GET"):
        libs=Librarian.objects.all()
        libs_serialize=LibrarianSerialize(libs,many=True)
        return JsonResponse(libs_serialize.data,safe=False)

@csrf_exempt
def Librarianview(request,fetchid):
    try:
        libs=Librarian.objects.get(id=fetchid)
        
        if (request.method=="GET"):
            lib_serializer=LibrarianSerialize(libs)
            return JsonResponse(lib_serializer.data,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            libs.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):
            mydata=JSONParser().parse(request)
            lib_serialize=LibrarianSerialize(libs,data=mydata)
            if (lib_serialize.is_valid()):
                lib_serialize.save()
                return JsonResponse(lib_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(lib_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid librarian Id",status=status.HTTP_404_NOT_FOUND)@csrf_exempt

@csrf_exempt
def searchapi(request):
    try:
        getlcode=request.POST.get("Lcode")
        getpat=Librarian.objects.filter(Lcode=getlcode)
        lib_s=LibrarianSerialize(getpat,many=True)
        return render(request,"search.html",{"data":lib_s.data})
       
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid librarian",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update_searchapi(request):
    try:
        getlcode=request.POST.get("Lcode")
        getpat=Librarian.objects.filter(Lcode=getlcode)
        lib_s=LibrarianSerialize(getpat,many=True)
        return render(request,"update.html",{"data":lib_s.data})
       
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid librarian",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    print(getId)
    getlcode=request.POST.get("newLcode")
    print(getlcode)
    getname=request.POST.get("newName")
    print(getname)
    getadress=request.POST.get("newAddress")
    print(getadress)
    getemail=request.POST.get("newEmail")
    print(getemail)
    getphone=request.POST.get("newMobile")
    print(getphone)
    getpincode=request.POST.get("newPincode")
    print(getpincode)
    mydata={"Lcode":getlcode,"Name":getname,"Address":getadress,"Mobile":getphone,"Pincode":getpincode,"Email":getemail}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/librarian/viewapi/"+ getId
    requests.put(ApiLink,data=jsondata)
    return redirect(Viewalllibrarian)

@csrf_exempt
def delete_searchapi(request):
    try:
        getlcode=request.POST.get("Lcode")
        getpat=Librarian.objects.filter(Lcode=getlcode)
        lib_s=LibrarianSerialize(getpat,many=True)
        return render(request,"delete.html",{"data":lib_s.data})
       
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid librarian",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/librarian/viewapi/"+ getId
    requests.delete(ApiLink)
    return redirect(Viewalllibrarian)