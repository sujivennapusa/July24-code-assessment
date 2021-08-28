from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from student.serializers import StudentSerializer
from student.models import Student
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.




def addata(request):
    return render(request,"index.html")

def viewall(request):
    fetchdata=requests.get("http://127.0.0.1:8000/student/viewall/").json()
    return render(request,"viewstudent.html",{"data":fetchdata})

def searchno(request):
    return render(request,"searchstudent.html")


def updation(request):
    return render(request,"updatestudent.html")

def deletion(request):
    return render(request,"deletestudent.html")









@csrf_exempt
def addstudent(request):
    if(request.method=="POST"):
        
        #mydict=JSONParser().parse(request)
        student_serialize=StudentSerializer(data=request.POST)
        if (student_serialize.is_valid()):
            student_serialize.save()
            return redirect(viewall)
            return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)




@csrf_exempt
def student_list(request):
    if(request.method=="GET"):
        students=Student.objects.all()
        student_serializer=StudentSerializer(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)


@csrf_exempt
def student_details(request, id):
    try:
        students=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        student_serializer=StudentSerializer(students)
        return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        students.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        student_serialize=StudentSerializer(students,data=mydict)
        if (student_serialize.is_valid()):
            student_serialize.save()
            return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
        


@csrf_exempt
def searchapi(request):
    try:
        getno=request.POST.get("adminno")
        getstudent=Student.objects.filter(adminno=getno)
        student_serializer=StudentSerializer(getstudent,many=True)
        return render(request,"searchstudent.html",{"data":student_serializer.data})
        return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    
    except Student.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def updatesearchapi(request):
    try:
        getno=request.POST.get("adminno")
        getstudent=Student.objects.filter(adminno=getno)
        student_serializer=StudentSerializer(getstudent,many=True)
        return render(request,"updatestudent.html",{"data":student_serializer.data})
        return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Student.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def updatedataread(request):
    getnewid=request.POST.get("newid")
    getnewname=request.POST.get("newname")
    getnewroll=request.POST.get("newroll")
    getnewadmin=request.POST.get("newadmin")
    getnewcollege=request.POST.get("newcollege")
    getnewparent=request.POST.get("newparent")
    getnewmob=request.POST.get("newmob")
    getnewdepart=request.POST.get("newdepart")

    mydata={'id':getnewid,'name':getnewname,'rollno':getnewroll,'adminno':getnewadmin,'college':getnewcollege,'parent':getnewparent,'mobnum':getnewmob,'department':getnewdepart}
    jsondata=json.dumps(mydata)
    print(jsondata)
    apilink="http://127.0.0.1:8000/student/viewone/" + getnewid
    requests.put(apilink,data=jsondata)
    return HttpResponse("data updated successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getno=request.POST.get("adminno")
        getstudent=Student.objects.filter(adminno=getno)
        student_serializer=StudentSerializer(getstudent,many=True)
        return render(request,"deletestudent.html",{"data":student_serializer.data})
        return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Student.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def deletedataread(request):
    getnewid=request.POST.get("newid")

    apilink="http://127.0.0.1:8000/student/viewone/" + getnewid
    requests.delete(apilink)
    return HttpResponse("data deleted successfully")



