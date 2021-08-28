from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from faculty.models import Faculty
from faculty.serializers import FacultySerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def searchapi(request):
    try:
        getfacultycode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getfacultycode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"search.html",{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid faculty code")
    except:
        return HttpResponse("something went wrong")

def facsearch(request):
    return render(request,'search.html')
def facultyviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/faculty/viewall/").json
    return render(request,'viewall.html',{"data":fetchdata})

def facultyupdate(request):
    return render(request,'update.html')


def facultyregister(request):
    return render(request,'registerf.html')

def facultydelete(request):
    return render(request,'delete.html')

@csrf_exempt
def addfaculty(request):
    if (request.method=="POST"):
        getcode=int(request.POST.get('fcode'))
        getname=request.POST.get('name')
        getdepartment=request.POST.get('department')
        getaddress=request.POST.get('address')
        getmobilenumber=int(request.POST.get('mobilenumber'))
        getusername=request.POST.get('username')
        getpassword=request.POST.get('password')
        mydata={'fcode':getcode,'name':getname,'department':getdepartment,'address':getaddress,'mobilenumber':getmobilenumber,'username':getusername,'password':getpassword}


        #mydata=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(data=mydata)
        
        if (faculty_serialize.is_valid()):
            faculty_serialize.save()
            return redirect(facultyviewss)
            #return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def faculty_all(request):
    if(request.method=="GET"):
        k=Faculty.objects.all()
        faculty_serializer=FacultySerializer(k,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)

@csrf_exempt
def faculty_single(request,fetchid):
    # try:
    sh=Faculty.objects.get(id=fetchid)

    
    if(request.method=="GET"):
        faculty_serialize=FacultySerializer(sh)
        return JsonResponse(faculty_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(sh,data=mydata)

        if(faculty_serialize.is_valid()):
            faculty_serialize.save()
            return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(faculty_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    # except Faculty.DoesNotExist:
    #     return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def updatesearchapi(request):
    try:
        getfacultycode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getfacultycode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"update.html",{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid faculty code")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getcode=request.POST.get('newfcode')
        getname=request.POST.get('newname')
        getdepartment=request.POST.get('newdepartment')
        getaddress=request.POST.get('newaddress')
        getmobilenumber=request.POST.get('newmobilenumber')
        mydata={'fcode':getcode,'name':getname,'department':getdepartment,'address':getaddress,'mobilenumber':getmobilenumber}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/faculty/view/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

@csrf_exempt
def deletesearchapi(request):
    try:
        getfacultycode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getfacultycode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        # return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"delete.html",{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid faculty code")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        
        ApiLink="http://localhost:8000/faculty/view/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")