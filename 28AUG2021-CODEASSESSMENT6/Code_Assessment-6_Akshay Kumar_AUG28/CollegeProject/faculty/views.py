
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from faculty.models import Faculty
from faculty.fac_serializers import FacultySerializers
from rest_framework import status
import requests,json


def faculty(request):
    return render(request,'index.html')

def viewFaculty(request):
    fetch = requests.get("http://127.0.0.1:8000/faculty/viewall/").json()
    return render(request,'view.html',{"data":fetch})
def updateFaculty(request):
    return render(request,'update.html')
def deleteFaculty(request):
    return render(request,'delete.html')
def searchFaculty(request):
    return render(request,'search.html')



@csrf_exempt
def search_api(request):
    try:
        getFcode = request.POST.get("fcode")
        getCode = Faculty.objects.filter(fcode = getFcode )
        fact_serializer = FacultySerializers(getCode,many=True)
        return render(request,'search.html',{"data":fact_serializer.data})
        
    except:
        return HttpResponse("No Faculty found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_search(request):
    try:
        getFcode = request.POST.get("fcode")
        getCode = Faculty.objects.filter(fcode = getFcode )
        fact_serializer = FacultySerializers(getCode,many=True)
        return render(request,'update.html',{"data":fact_serializer.data})
        
    except:
        return HttpResponse("No Faculty found",status=status.HTTP_404_NOT_FOUND)
    


@csrf_exempt
def update_data(request):
    getnewid = request.POST.get("newid")
    getfcode = request.POST.get("newfcode")
    getdept = request.POST.get("newdept")
    getname = request.POST.get("newname")
    getaddress = request.POST.get("newaddress")
    getmobno = request.POST.get("newmobno")
    
    mydata= {"fcode":getfcode,"dept":getdept,"name":getname,"address":getaddress,"mobno":getmobno}
    jsondata = json.dumps(mydata)
    apilink = "http://127.0.0.1:8000/faculty/view/"+getnewid
    requests.put(apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")

@csrf_exempt
def delete_search(request):
    try:
        getFcode = request.POST.get("fcode")
        getCode = Faculty.objects.filter(fcode = getFcode )
        fact_serializer = FacultySerializers(getCode,many=True)
        return render(request,'delete.html',{"data":fact_serializer.data})
        
    except:
        return HttpResponse("No Faculty found",status=status.HTTP_404_NOT_FOUND)
    
   


@csrf_exempt
def delete_data(request):
    getnewid = request.POST.get("newid")
    apilink = "http://127.0.0.1:8000/faculty/view/"+getnewid
    requests.delete(apilink)
    return HttpResponse("Data deleted Successfully")

def home(request):
    return render(request,'home.html')


@csrf_exempt
def addFaculty(request):
    if(request.method == "POST"):
        # mydict = JSONParser().parse(request)
        faculty_serializer = FacultySerializers(data = request.POST)
        if(faculty_serializer.is_valid()):
            faculty_serializer.save()
            return JsonResponse(faculty_serializer.data)

        else:
            return HttpResponse("Error in Serialization")

    else:
        return HttpResponse("GET Method not allowed")

@csrf_exempt
def listFaculty(request):
    if(request.method == "GET"):
        faculty = Faculty.objects.all()
        f_serializer = FacultySerializers(faculty, many = True)
        return JsonResponse(f_serializer.data, safe=False )

@csrf_exempt
def view(request,id):
    try:
        faculty = Faculty.objects.get(id = id)
        if(request.method == "GET"):
            f_serializer = FacultySerializers(faculty)
            return JsonResponse(f_serializer.data, safe=False)

        if(request.method == "DELETE"):
        
            faculty.delete()
            return HttpResponse("Deleted")

        if(request.method == "PUT"):
            mydata = JSONParser().parse(request)
            fa_serialize = FacultySerializers(faculty,data = mydata)
            if(fa_serialize.is_valid()):
                fa_serialize.save()
                return JsonResponse(fa_serialize.data)

    except Faculty.DoesNotExist:
        return HttpResponse("Invalid Faculty ID")
    


    