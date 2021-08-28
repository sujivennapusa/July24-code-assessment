from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from student.serializer import StudentSerializer
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from student.models import Studentapp
import requests
import json



def addpage(request):
    return render(request,'add.html')

def viewpage(request):
    fetchdata=requests.get("http://127.0.0.1:8000/student/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})

def searchpage(request):
    return render(request,'search.html')

def updatepage(request):
    return render(request,'update.html')

def deletepage(request):
    return render(request,'delete.html')



@csrf_exempt
def student(request):
    if(request.method=="POST"):
        # studata=JSONParser().parse(request)
        Student_Serializer= StudentSerializer(data=request.POST)
        if(Student_Serializer.is_valid()):
            Student_Serializer.save()
            return redirect(viewpage)
    #         return JsonResponse(Student_Serializer.data,status=status.HTTP_200_OK)
    #     else:
    #         return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def student_list(request):
    if(request.method == "GET"):
        students = Studentapp.objects.all()
        Student_Serializer= StudentSerializer(students, many=True)
        return JsonResponse(Student_Serializer.data, safe=False)


@csrf_exempt
def studentdetail(request,id):
    try:
        students=Studentapp.objects.get(admno=id)
        if(request.method == "GET"):
            Student_Serializer=StudentSerializer(students)
            return JsonResponse(Student_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            students.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            studata=JSONParser().parse(request)
            Student_Serializer = StudentSerializer(students,data=studata)
            if(Student_Serializer.is_valid()):
                Student_Serializer.save()
                return JsonResponse(Student_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serialization")

    except Studentapp.DoesNotExist:
        return HttpResponse("Invalid Student admission number",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def search(request):
    try:
        getadmno = request.POST.get("admno")
        getstudent = Studentapp.objects.filter(admno=getadmno)
        Student_Serializer = StudentSerializer(getstudent,many=True)
        return render(request,'search.html',{"data":Student_Serializer.data})
    except Studentapp.DoesNotExist:
        return HttpResponse('Invalid Admission number')
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def apiupdate(request):
    try:
        getadmno = request.POST.get("admno")
        getstudent = Studentapp.objects.filter(admno=getadmno)
        Student_Serializer = StudentSerializer(getstudent,many=True)
        return render(request,'update.html',{"data":Student_Serializer.data})
    except Studentapp.DoesNotExist:
        return HttpResponse('Invalid Admission number')
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update(request):
    getid=request.POST.get("newid")
    getname = request.POST.get("newname")
    getrollno = request.POST.get("newrollno")
    getadmno = request.POST.get("newadmno")
    getcollege = request.POST.get("newcollege")
    getmobile = request.POST.get("newmobile")
    getdepartment = request.POST.get("newdepartment")
    
    mydata = {"id":getid,"name":getname,"rollno":getrollno,"admno":getadmno,"college":getcollege,"mobile":getmobile,"department":getdepartment}
    jsondata = json.dumps(mydata)
    print(jsondata)
    Apilink = "http://127.0.0.1:8000/faculty/view/"+str(getadmno)
    requests.put(Apilink, data=jsondata)
    return redirect(viewpage)

@csrf_exempt
def delete(request):
    
    getadmno = request.POST.get("newadmno")
    apilink = "http://127.0.0.1:8000/student/view/"+str(getadmno)
    requests.delete(apilink)
    return redirect(viewpage) 

@csrf_exempt
def apidelete(request):
    try:
        getadmno = request.POST.get("admno")
        getstudent = Studentapp.objects.filter(admno=getadmno)
        Student_Serializer = StudentSerializer(getstudent,many=True)
        return render(request,'delete.html',{"data":Student_Serializer.data})
    except Studentapp.DoesNotExist:
        return HttpResponse('Invalid Admission number')
    except:
        return HttpResponse("Something went wrong")
  