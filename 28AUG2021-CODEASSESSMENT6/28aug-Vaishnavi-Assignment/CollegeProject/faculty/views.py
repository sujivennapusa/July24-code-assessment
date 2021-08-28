from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from faculty.serializer import FacultySerializer
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from faculty.models import Facultyapp
import requests
import json



def addpagee(request):
    return render(request,'add1.html')

def viewpagee(request):
    fetchdata=requests.get("http://127.0.0.1:8000/faculty/viewall/").json()
    return render(request,'view1.html',{"data":fetchdata})

def searchpagee(request):
    return render(request,'search1.html')

def updatepagee(request):
    return render(request,'update1.html')

def deletepagee(request):
    return render(request,'delete1.html')

@csrf_exempt
def faculty(request):
    if(request.method=="POST"):
        # facdata=JSONParser().parse(request)
        Faculty_Serializer= FacultySerializer(data=request.POST)
        if(Faculty_Serializer.is_valid()):
            Faculty_Serializer.save()
            return redirect(viewpagee)
            # return JsonResponse(Faculty_Serializer.data,status=status.HTTP_200_OK)
    #     else:
    #         return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def faculty_list(request):
    if(request.method == "GET"):
        faculties = Facultyapp.objects.all()
        Faculty_Serializer= FacultySerializer(faculties, many=True)
        return JsonResponse(Faculty_Serializer.data, safe=False)


@csrf_exempt
def facultydetail(request,id):
    try:
        faculties=Facultyapp.objects.get(faculty_code=id)
        if(request.method == "GET"):
            Faculty_Serializer=FacultySerializer(faculties)
            return JsonResponse(Faculty_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            faculties.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            studata=JSONParser().parse(request)
            Faculty_Serializer = FacultySerializer(faculties,data=studata)
            if(Faculty_Serializer.is_valid()):
                Faculty_Serializer.save()
                return JsonResponse(Faculty_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serialization")

    except Facultyapp.DoesNotExist:
        return HttpResponse("Invalid Faculty code",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def searchp(request):
    try:
        getfaculty_code = request.POST.get("faculty_code")
        getfaculty = Facultyapp.objects.filter(faculty_code=getfaculty_code)
        Faculty_Serializer = FacultySerializer(getfaculty,many=True)
        return render(request,'search1.html',{"data":Faculty_Serializer.data})
    except Facultyapp.DoesNotExist:
        return HttpResponse('Invalid Faculty code')
    except:
        return HttpResponse("Something went wrong")


@csrf_exempt
def apiupdatee(request):
    try:
        getfaculty_code = request.POST.get("faculty_code")
        getfaculty = Facultyapp.objects.filter(faculty_code=getfaculty_code)
        Faculty_Serializer = FacultySerializer(getfaculty,many=True)
        return render(request,'update.html',{"data":Faculty_Serializer.data})
    except Facultyapp.DoesNotExist:
        return HttpResponse('Invalid Faculty code')
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def updatee(request):
    getid=request.POST.get("newid")
    getfaculty_code = request.POST.get("newfaculty_code")
    getname = request.POST.get("newname")
    getdepartment = request.POST.get("newdepartment")
    getaddress = request.POST.get("newaddress")
    getmobilenumber = request.POST.get("newmobilenumber")
    
    mydata = {"id":getid,"faculty_code":getfaculty_code,"name":getname,"department":getdepartment,"address":getaddress,"mobilenumber":getmobilenumber}
    jsondata = json.dumps(mydata)
    print(jsondata)
    Apilink = "http://127.0.0.1:8000/faculty/view/"+str(getfaculty_code)
    requests.put(Apilink, data=jsondata)
    return redirect(viewpagee)


@csrf_exempt
def deletee(request):
    
    getfaculty_code = request.POST.get("newfaculty_code")
    apilink = "http://127.0.0.1:8000/faculty/view/"+str(getfaculty_code)
    requests.delete(apilink)
    return redirect(viewpagee)

@csrf_exempt
def apideletee(request):
    try:
        getfaculty_code = request.POST.get("faculty_code")
        getfaculty = Facultyapp.objects.filter(faculty_code=getfaculty_code)
        Faculty_Serializer = FacultySerializer(getfaculty,many=True)
        return render(request,'delete1.html',{"data":Faculty_Serializer.data})
    except Facultyapp.DoesNotExist:
        return HttpResponse('Invalid Faculty code')
    except:
        return HttpResponse("Something went wrong")

