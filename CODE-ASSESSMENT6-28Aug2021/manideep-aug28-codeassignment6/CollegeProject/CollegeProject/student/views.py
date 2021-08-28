from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from student.models import College
from student.serializers import CollegeSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

def register(request):
    return render(request,'register.html')


def stdsearch(request):
    return render(request,'search.html')
def studentviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/student/viewall/").json
    return render(request,'viewall.html',{"data":fetchdata})

def studentupdate(request):
    return render(request,'update.html')
def studentdelete(request):
    return render(request,'delete.html')

@csrf_exempt
def searchapi(request):
    try:
        getstudentadmnno=request.POST.get("admnno")
        getstudent=College.objects.filter(admnno=getstudentadmnno)
        student_serializer=CollegeSerializer(getstudent,many=True)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"search.html",{"data":student_serializer.data})
    except College.DoesNotExist:
        return HttpResponse("Invalid faculty code")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def addstudent(request):
    if (request.method=="POST"):
        print(request.POST)
        # mydata=JSONParser().parse(request)
        std_serialize=CollegeSerializer(data=request.POST)
        
        if (std_serialize.is_valid()):
            std_serialize.save()
            return JsonResponse(std_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def student_all(request):
    if(request.method=="GET"):
        k=College.objects.all()
        std_serializer=CollegeSerializer(k,many=True)
        return JsonResponse(std_serializer.data,safe=False)

@csrf_exempt
def student_single(request,fetchid):
    try:
        sh=College.objects.get(id==fetchid)
    
        
        if(request.method=="GET"):
            std_serialize=CollegeSerializer(sh)
            return JsonResponse(std_serialize.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            sh.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            std_serialize=CollegeSerializer(sh,data=mydata)

            if(std_serialize.is_valid()):
                std_serialize.save()
                return JsonResponse(std_serialize.data,status=status.HTTP_200_OK)

    except College.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def updatesearchapi(request):
    try:
        getstudentadmnno=request.POST.get("admnno")
        getstudent=College.objects.filter(admnno=getstudentadmnno)
        student_serializer=CollegeSerializer(getstudent,many=True)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"update.html",{"data":student_serializer.data})
    except College.DoesNotExist:
        return HttpResponse("Invalid faculty code")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')     
        getnewname=request.POST.get('newname')
        getnewadmnno=request.POST.get('newadmnno')
        getnewrollno=request.POST.get('newrollno')
        getnewcollege=request.POST.get('newcollege')
        getnewparentname=request.POST.get('newparentname')
        getnewmobilenumber=request.POST.get('newmobilenumber')
        getnewdepartment1=request.POST.get('newdepartment1')
        mydata={"name":getnewname,"admnno":getnewadmnno,"rollno":getnewrollno,"college":getnewcollege,"parentname":getnewparentname,"mobilenumber":getnewmobilenumber,"department1":getnewdepartment1}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/student/view/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

@csrf_exempt
def deletesearchapi(request):
    try:
        getstudentadmnno=request.POST.get("admnno")
        getstudent=College.objects.filter(admnno=getstudentadmnno)
        student_serializer=CollegeSerializer(getstudent,many=True)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"delete.html",{"data":student_serializer.data})
    except College.DoesNotExist:
        return HttpResponse("Invalid faculty code")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/student/view/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")

