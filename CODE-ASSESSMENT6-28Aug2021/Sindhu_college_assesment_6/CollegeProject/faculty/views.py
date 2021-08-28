from django.shortcuts import redirect,render
from faculty.models import Faculty
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from faculty.serializers import FacultySerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
def delete_faculty_view(request):
    return render(request,'del.html')
@csrf_exempt
def deleteapi(request):
    try:
        getfcode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getfcode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        print(faculty_serializer.data)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"del.html",{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid fcode",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
@csrf_exempt
def delete_data_read(request):
    getnewid=request.POST.get("newid")
    # getnewfcode=request.POST.get("newfcode")
    # getnewname=request.POST.get("newname")
    # getnewdept=request.POST.get("newdept")
    # getnewaddress=request.POST.get("newaddress")
    # getnewmobileno=request.POST.get("newmobileno")
    # mydata={'fcode':getnewfcode,'name':getnewname,'dept':getnewdept,'address':getnewaddress,
    #         'mobileno':getnewmobileno}
    # jsondata=json.dumps(mydata)
    # print(jsondata)
    Apilink="http://127.0.0.1:8000/faculty/view/"+getnewid
    requests.delete(Apilink)
    return HttpResponse("Data has deleted succesfully")
def update_faculty_view(request):
    return render(request,'up.html')
@csrf_exempt
def updateapi(request):
    try:
        getfcode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getfcode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        print(faculty_serializer.data)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"up.html",{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid fcode",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
@csrf_exempt
def update_data_read(request):
    getnewid=request.POST.get("newid")
    getnewfcode=request.POST.get("newfcode")
    getnewname=request.POST.get("newname")
    getnewdept=request.POST.get("newdept")
    getnewaddress=request.POST.get("newaddress")
    getnewmobileno=request.POST.get("newmobileno")
    mydata={'fcode':getnewfcode,'name':getnewname,'dept':getnewdept,'address':getnewaddress,
            'mobileno':getnewmobileno}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/faculty/view/"+getnewid
    requests.put(Apilink,data=jsondata)
    return HttpResponse("Data has updated succesfully")
def search_faculty_view(request):
    return render(request,'sh.html')
@csrf_exempt
def searchapi(request):
    try:
        getfcode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getfcode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        print(faculty_serializer.data)
        # return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"sh.html",{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid fcode",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
def viewall_faculty_view(request):
    fetchdata=requests.get("http://127.0.0.1:8000/faculty/viewall/").json()
    return render(request,'all.html',{"data":fetchdata})
def add_faculty_view(request):
    return render(request,'reg.html')
@csrf_exempt
def faculty_list(request):
    if(request.method=="GET"):
        facultys=Faculty.objects.all()
        faculty_serializer=FacultySerializer(facultys,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)
@csrf_exempt
def faculty_create(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(data=request.POST)
        if(faculty_serialize.is_valid()):
            faculty_serialize.save()
            return redirect(viewall_faculty_view)
            # return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def faculty_details(request,id):
    try:
        facultys=Faculty.objects.get(id=id)
        if(request.method=="GET"):
            faculty_serializer=FacultySerializer(facultys)
            return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            facultys.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            faculty_serialize=FacultySerializer(facultys,data=mydata)
            if(faculty_serialize.is_valid()):
                faculty_serialize.save()
                return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(faculty_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)

