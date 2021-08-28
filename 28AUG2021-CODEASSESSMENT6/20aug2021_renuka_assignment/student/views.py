
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from student.serializers import StudentSerializer
import json
from student.models import Student
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
@csrf_exempt
def studentaddpage(request):
    if (request.method=="POST"):
        gname=request.POST.get("name")
        grollno=request.POST.get("rollno")
        gadmno=request.POST.get("admno")
        gcollege=request.POST.get("college")
        gparentname=request.POST.get("parentname")
        gmobilenumber=request.POST.get("mobilenumber")
        gdepartment=request.POST.get("department")
        mydict={'name':gname,'rollno':grollno,'admno':gadmno,'college':gcollege,'parentname':gparentname,'mobilenumber':gmobilenumber,'department':gdepartment}
        student_serialize=StudentSerializer(data=mydict)
        if (student_serialize.is_valid()):
            student_serialize.save()
            return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)
    # if (request.method=="POST"):
    #     student_serialize=StudentSerializer(data=request.POST)
    #     if (student_serialize.is_valid()):
    #         student_serialize.save()
    #         return redirect(stu_view)
    #     else:
    #         return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)
    

@csrf_exempt
def student_list(request):
    if (request.method=="GET"):
        students=Student.objects.all()
        student_serializer=StudentSerializer(flats,many=True)
        return JsonResponse(student_serializer.data,safe=False)
@csrf_exempt
def student_details(request,fetchid):
    try:
        students=Student.objects.get(id=fetchid)
    except Student.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        student_serializer=StudentSerializer(students)
        return JsonResponse(student_serializer.data,safe=False)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        student_serialize=StudentSerializer(students,data=mydict)
        if (student_serialize.is_valid()):
            student_serialize.save()
            return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(student_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    if(request.method=="DELETE"):
        students.delete()
        return HttpResponse("Deleted",status=status.HTTP_404_NOT_FOUND)


def student_view(request):
    return render(request,'index.html')

def stu_view(request):
    fetchdata=requests.get("http://localhost:8000/student/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})

def search_view(request):
    return render(request,'search.html')

def update_view(request):
    return render(request,'update.html')

def delete_view(request):
    return render(request,'delete.html')

@csrf_exempt
def searchapi(request):
    try:
        getadmno=request.POST.get("admno")
        getstudent=Student.objects.filter(admno=getadmno)
        student_serializer=StudentSerializer(getstudent,many=True)
        return render(request,"search.html",{"data":student_serializer.data})
    except Student.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def updatesearchapi(request):
    try:
        gadmno=request.POST.get("admno")
        getstudent=Student.objects.filter(admno=gadmno)
        student_serializer=StudentSerializer(getstudent,many=True)
        return render(request,'update.html',{"data":student_serializer.data})
    except Student.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")


@csrf_exempt
def update_data_read(request):
    gadmno=request.POST.get("newadmno")
    gname=request.POST.get("newname")
    getid=request.POST.get("newid")
    grollno=request.POST.get("newrollno")
    gcollege=request.POST.get("newcollege")
    gmobilenumber=request.POST.get("newmobilenumber")
    gparentname=request.POST.get("newparentname")
    gdepartment=request.POST.get("newdepartment")
    mydata={'admno':gadmno,'name':gname,'rollno':grollno,'college':gcollege,'mobilenumber':gmobilenumber,'parentname':gparentname,'department':gdepartment}
    jsondata=json.dumps(mydata)
    Apilink="http://localhost:8000/student/viewstudents/" + getid
    print(jsondata)
    requests.put(Apilink,data=jsondata)
    return HttpResponse("data updated successfully")


@csrf_exempt
def delete_data_read(request):
    getnewid=request.POST.get("newid")
   
    Apilink="http://localhost:8000/student/viewflats/" + getnewid
    requests.delete(Apilink)
    return HttpResponse("data deleted successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        gadmno=request.POST.get("admno")
        getstudent=Student.objects.filter(admno=gadmno)
        student_serializer=StudentSerializer(getstudent,many=True)
        return render(request,"delete.html",{"data":student_serializer.data})
       
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")