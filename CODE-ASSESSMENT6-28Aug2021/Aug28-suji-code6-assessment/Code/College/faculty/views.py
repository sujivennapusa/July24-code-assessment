from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from faculty.serializers import FacultySerializer
from faculty.models import Faculty
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
@csrf_exempt
def faculty_add(request):
    if request.method=="POST":
        # getCode=request.POST.get("facultycode")
        # getDepartment=request.POST.get("department")
        # getName=request.POST.get("fname")
        # getAddress=request.POST.get("address")
        # getMobileno=request.POST.get("mobileno")
        # mydata={"facultycode":getCode,"department":getDepartment,"fname":getName,"address":getAddress,"mobileno":getMobileno};
        # result=json.dumps(mydata)
        # return HttpResponse(result)
        mydata=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(data=mydata)
        if(faculty_serialize.is_valid()):
            faculty_serialize.save()
            return JsonResponse(faculty_serialize.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No get method allowed")

@csrf_exempt
def faculty_list(request):
    if(request.method=="GET"):
        faculties=Faculty.objects.all()
        faculty_serializer=FacultySerializer(faculties,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)
      
@csrf_exempt
def faculty_details(request,fetchid):
    try:
        faculties=Faculty.objects.get(id=fetchid)
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid Faculty Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        faculty_serialize=FacultySerializer(faculties)
        return JsonResponse(faculty_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        faculties.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   

    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(faculties,data=mydata)
        if(faculty_serialize.is_valid()):
           faculty_serialize.save()
           return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(faculty_serialize.errors,status=status.HTTP_400_BAD_REQUEST)   

def faculty_interface(request):
    return render(request,'faculty.html')  
def view_list(request):
    fetchdata=requests.get("http://127.0.0.1:8000/faculty/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})
    

def update_list(request):
    return render(request,'update.html')  
def delete_list(request):
    return render(request,'delete.html') 

def search_list(request):
    return render(request,'search.html')     

@csrf_exempt
def searchapi(request):
    try:
        getCode=request.POST.get("facultycode")
        getFaculty=Faculty.objects.filter(facultycode=getCode)
        faculty_serialize=FacultySerializer(getFaculty,many=True)
        return render(request,"search.html",{"data":faculty_serialize.data})
        #return JsonResponse(faculty_serialize.data,safe=False,status=status.HTTP_200_OK)
    except Flat.DoesNotExist:
        return HttpResponse("Invalid faculty code",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")

@csrf_exempt
def updateapi(request):
    try:
        getCode=request.POST.get("facultycode")
        getFaculty=Faculty.objects.filter(facultycode=getCode)
        faculty_serialize=FacultySerializer(getFaculty,many=True)
        return render(request,"update.html",{"data":faculty_serialize.data})
        #return JsonResponse(faculty_serialize.data,safe=False,status=status.HTTP_200_OK)
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid faculty code",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")   

@csrf_exempt
def update_read(request):
    getNewid=request.POST.get("newid")
    getNewfacultycode=request.POST.get("newfacultycode") 
    getNewdepartment=request.POST.get("newdepartment") 
    getNewname=request.POST.get("newfname") 
    
    getNewaddress=request.POST.get("newaddress")
    getnewmobileno=request.POST.get("newmobileno")
    
    mydata={'facultycode':newfacultycode,'department':getNewdepartment,'fname':getNewname,'address':getNewaddress,'mobileno':getNewmobileno}
    jsondata=json.dumps(mydata) 
    print(jsondata)
    Apilink="http://127.0.0.1:8000/Faculty/view/"+getNewid       
    requests.put(Apilink,data=jsondata)
    return HttpResponse("Data has Updated successfully")    

@csrf_exempt
def deleteapi(request):
    try:
        
        getCode=request.POST.get("facultycode")
        getFaculty=Faculty.objects.filter(facultycode=getCode)
        faculty_serialize=FacultySerializer(getFaculty,many=True)
        return render(request,"delete.html",{"data":faculty_serialize.data})
        #return JsonResponse(faculty_serialize.data,safe=False,status=status.HTTP_200_OK)
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid faculty code",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")      


@csrf_exempt
def delete_read(request):
    getNewid=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/Faculty/view/"+getNewid       
    requests.delete(Apilink)
    return HttpResponse("Data has deleted successfully")            

