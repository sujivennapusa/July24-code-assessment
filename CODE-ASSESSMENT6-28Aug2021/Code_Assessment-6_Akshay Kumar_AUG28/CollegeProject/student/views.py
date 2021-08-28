
from re import S
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from student.models import Student
from student.student_serializers import StudentSerializer
from rest_framework import status
import requests,json


def student(request):
    return render(request,'index1.html')

def viewStudent(request):
    fetch = requests.get("http://127.0.0.1:8000/student/viewall/").json()
    return render(request,'view1.html',{"data":fetch})
def updateStudent(request):
    return render(request,'update1.html')
def deleteStudent(request):
    return render(request,'delete1.html')
def searchStudent(request):
    return render(request,'search1.html')



@csrf_exempt
def search_api(request):
    try:
        getadmno = request.POST.get("admno")
        getadm = Student.objects.filter(admno = getadmno )
        adm_serializer = StudentSerializer(getadm,many=True)
        return render(request,'search1.html',{"data":adm_serializer.data})
        
    except:
        return HttpResponse("No Students found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_search(request):
    try:
        getadmno = request.POST.get("admno")
        getadm = Student.objects.filter(admno = getadmno )
        adm_serializer = StudentSerializer(getadm,many=True)
        return render(request,'update1.html',{"data":adm_serializer.data})
        
    except:
        return HttpResponse("No Students found",status=status.HTTP_404_NOT_FOUND)
    


@csrf_exempt
def update_data(request):
    getnewid = request.POST.get("newid")
    getname = request.POST.get("newname")
    getrollno = request.POST.get("newrollno")
    getadmno = request.POST.get("newadmno")
    getcollege = request.POST.get("newcollege")
    getparent = request.POST.get("newparent")
    getmobno = request.POST.get("newmobno")
    getdept = request.POST.get("newdept")
    mydata= {"name":getname,"rollno":getrollno,"admno":getadmno,"college":getcollege,"parent":getparent,"mobno":getmobno,"dept":getdept}
    jsondata = json.dumps(mydata)
    apilink = "http://127.0.0.1:8000/student/view/"+getnewid
    requests.put(apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")

@csrf_exempt
def delete_search(request):
    try:
        getadmno = request.POST.get("admno")
        getadm = Student.objects.filter(admno = getadmno )
        adm_serializer = StudentSerializer(getadm,many=True)
        return render(request,'delete1.html',{"data":adm_serializer.data})
        
    except:
        return HttpResponse("No Students found",status=status.HTTP_404_NOT_FOUND)
    
   


@csrf_exempt
def delete_data(request):
    getnewid = request.POST.get("newid")
    apilink = "http://127.0.0.1:8000/student/view/"+getnewid
    requests.delete(apilink)
    return HttpResponse("Data deleted Successfully")


@csrf_exempt
def addStudent(request):
    if(request.method == "POST"):
        # mydict = JSONParser().parse(request)
        stud_serializer = StudentSerializer(data = request.POST)
        if(stud_serializer.is_valid()):
            stud_serializer.save()
            return JsonResponse(stud_serializer.data)

        else:
            return HttpResponse("Error in Serialization")

    else:
        return HttpResponse("GET Method not allowed")

@csrf_exempt
def listStudent(request):
    if(request.method == "GET"):
        student = Student.objects.all()
        stud_serializer = StudentSerializer(student, many = True)
        return JsonResponse(stud_serializer.data, safe=False )

@csrf_exempt
def view(request,id):
    try:
        student = Student.objects.get(id = id)
        if(request.method == "GET"):
            stud_serializer = StudentSerializer(student)
            return JsonResponse(stud_serializer.data, safe=False)

        if(request.method == "DELETE"):
            student.delete()
            return HttpResponse("Deleted")

        if(request.method == "PUT"):
            mydata = JSONParser().parse(request)
            c_serialize = StudentSerializer(student,data = mydata)
            if(c_serialize.is_valid()):
                c_serialize.save()
                return JsonResponse(c_serialize.data)

    except Student.DoesNotExist:
        return HttpResponse("Invalid Student ID")
    


    