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
def student_add(request):
    if request.method=="POST":
        # getName=request.POST.get("sname")
        # getRollno=request.POST.get("rollno")
        # getAdmno=request.POST.get("admno")
        # getCollege=request.POST.get("college")
        # getParent=request.POST.get("parent")
        # getNumber=request.POST.get("mobileno")
        # getDept=request.POST.get("department")
        # mydata={"sname":getName,"rollno":getRollno,"admno":getAdmno,"college":getCollege,"parent":getParent,"mobileno":getNumber,"department":getDept};
        # result=json.dumps(mydata)
        # return HttpResponse(result)

        
        # mydata=JSONParser().parse(request)
        student_serialize=StudentSerializer(data=request.POST)
        if(student_serialize.is_valid()):
           student_serialize.save()
           #return JsonResponse(student_serialize.data)
           return redirect(view_list)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No get method allowed")

@csrf_exempt
def student_list(request):
    if(request.method=="GET"):
        students=Student.objects.all()
        student_serializer=StudentSerializer(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)

@csrf_exempt
def student_details(request,fetchid):
    try:
        students=Student.objects.get(id=fetchid)
    except Student.DoesNotExist:
        return HttpResponse("Invalid Student Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        student_serialize=StudentSerializer(students)
        return JsonResponse(student_serialize.data,safe=False,status=status.HTTP_200_OK)


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

def student_interface(request):
    return render(request,'student.html') 
def view_list(request):
    fetchdata=requests.get("http://127.0.0.1:8000/student/viewall/").json()
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
        getAdmno=request.POST.get("admno")
        getStudent=Student.objects.filter(admno=getAdmno)
        student_serialize=StudentSerializer(getStudent,many=True)
        return render(request,"search.html",{"data":student_serialize.data})
        # return JsonResponse(student_serialize.data,safe=False,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return HttpResponse("Invalid student admno",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")

@csrf_exempt
def updateapi(request):
    try:
        getAdmno=request.POST.get("admno")
        getStudent=Student.objects.filter(admno=getAdmno)
        student_serialize=StudentSerializer(getStudent,many=True)
        return render(request,"update.html",{"data":student_serialize.data})
        # return JsonResponse(student_serialize.data,safe=False,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return HttpResponse("Invalid student admno",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")      

@csrf_exempt
def update_read(request):
    getNewid=request.POST.get("newid")
    getNewsname=request.POST.get("newsname") 
    getNewrollno=request.POST.get("newrollno")
    getNewadmno=request.POST.get("newadmno")
    getNewcollege=request.POST.get("newcollege")
    getNewparent=request.POST.get("newparent")
    getNewmobileno=request.POST.get("newmobileno")
    getNewdepartment=request.POST.get("newdepartment")
    mydata={'sname':getNewsname,'rollno':getNewrollno,'admno':getNewadmno,'college':getNewcollege,'parent':getNewparent,'mobileno':getNewmobileno,'department':getNewdepartment}
    jsondata=json.dumps(mydata) 
    print(jsondata)
    Apilink="http://127.0.0.1:8000/student/view/"+getNewid       
    requests.put(Apilink,data=jsondata)
    return HttpResponse("Data has Updated successfully")                     


@csrf_exempt
def deleteapi(request):
    try:
        
        getAdmno=request.POST.get("admno")
        getStudent=Student.objects.filter(admno=getAdmno)
        student_serialize=StudentSerializer(getStudent,many=True)
        return render(request,"delete.html",{"data":student_serialize.data})
        #return JsonResponse(student_serialize.data,safe=False,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return HttpResponse("Invalid admno",status=status.HTTP_404_NOT_FOUND)  
    except:
        return HttpResponse("Something is wrong")      


@csrf_exempt
def delete_read(request):
    getNewid=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/student/view/"+getNewid       
    requests.delete(Apilink)
    return HttpResponse("Data has deleted successfully")        
