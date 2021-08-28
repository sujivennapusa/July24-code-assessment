from django.shortcuts import redirect,render
from student.models import Student
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from student.serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.

def delete_student_view(request):
    return render(request,'delete.html')
@csrf_exempt
def deleteapi(request):
    try:
        getadmno=request.POST.get("admno")
        getstudent=Student.objects.filter(admno=getadmno)
        student_serializer=StudentSerializer(getstudent,many=True)
        print(student_serializer.data)
        # return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"delete.html",{"data":student_serializer.data})
    except Student.DoesNotExist:
        return HttpResponse("Invalid admno",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
@csrf_exempt
def delete_data_read(request):
    getnewid=request.POST.get("newid")
    # getnewname=request.POST.get("newname")
    # getnewadmno=request.POST.get("newadmno")
    # getnewrollno=request.POST.get("newrollno")
    # getnewcollege=request.POST.get("newcollege")
    # getnewparentname=request.POST.get("newparentname")
    # getnewmobileno=request.POST.get("newmobileno")
    # getnewdept=request.POST.get("newdept")
    # mydata={'name':getnewname,'admno':getnewadmno,'rollno':getnewrollno,'college':getnewcollege,
    #         'parentname':getnewparentname,'mobileno':getnewmobileno,'dept':getnewdept}
    # jsondata=json.dumps(mydata)
    # print(jsondata)
    Apilink="http://127.0.0.1:8000/student/view/"+getnewid
    requests.delete(Apilink)
    return HttpResponse("Data has deleted succesfully")

def update_student_view(request):
    return render(request,'update.html')
@csrf_exempt
def updateapi(request):
    try:
        getadmno=request.POST.get("admno")
        getstudent=Student.objects.filter(admno=getadmno)
        student_serializer=StudentSerializer(getstudent,many=True)
        print(student_serializer.data)
        # return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"update.html",{"data":student_serializer.data})
    except Student.DoesNotExist:
        return HttpResponse("Invalid admno",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
@csrf_exempt
def update_data_read(request):
    getnewid=request.POST.get("newid")
    getnewname=request.POST.get("newname")
    getnewadmno=request.POST.get("newadmno")
    getnewrollno=request.POST.get("newrollno")
    getnewcollege=request.POST.get("newcollege")
    getnewparentname=request.POST.get("newparentname")
    getnewmobileno=request.POST.get("newmobileno")
    getnewdept=request.POST.get("newdept")
    mydata={'name':getnewname,'admno':getnewadmno,'rollno':getnewrollno,'college':getnewcollege,
            'parentname':getnewparentname,'mobileno':getnewmobileno,'dept':getnewdept}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/student/view/"+getnewid
    requests.put(Apilink,data=jsondata)
    return HttpResponse("Data has updated succesfully")
def search_student_view(request):
    return render(request,'sh.html')
@csrf_exempt
def searchapi(request):
    try:
        getfcode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getfcode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        print(faculty_serializer.data)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"sh.html",{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid fcode",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
def add_student_view(request):
    return render(request,'sub.html')
def viewall_student_view(request):
    fetchdata=requests.get("http://127.0.0.1:8000/student/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
@csrf_exempt
def student_list(request):
    if(request.method=="GET"):
        students=Student.objects.all()
        student_serializer=StudentSerializer(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)
@csrf_exempt
def student_create(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        student_serialize=StudentSerializer(data=request.POST)
        if(student_serialize.is_valid()):
            student_serialize.save()
            return redirect(viewall_student_view)
            # return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def student_details(request,id):
    try:
        students=Student.objects.get(id=id)
        if(request.method=="GET"):
            student_serializer=StudentSerializer(students)
            return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            students.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            student_serialize=StudentSerializer(students,data=mydata)
            if(student_serialize.is_valid()):
                student_serialize.save()
                return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(student_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)