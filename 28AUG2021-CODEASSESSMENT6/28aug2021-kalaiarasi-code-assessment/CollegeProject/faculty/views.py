from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from faculty.serializers import FacultySerializer
from faculty.models import Faculty
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.


def addata(request):
    return render(request,"indexf.html")

def viewall(request):
    fetchdata=requests.get("http://127.0.0.1:8000/faculty/viewall/").json()
    return render(request,"viewfaculty.html",{"data":fetchdata})

def searchcode(request):
    return render(request,"searchfaculty.html")


def updation(request):
    return render(request,"updatefaculty.html")

def deletion(request):
    return render(request,"deletefaculty.html")



@csrf_exempt
def addfaculty(request):
    if(request.method=="POST"):
        
        # mydict=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(data=request.POST)
        if (faculty_serialize.is_valid()):
            faculty_serialize.save()
            return redirect(viewall)
            return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def faculty_list(request):
    if(request.method=="GET"):
        faculties=Faculty.objects.all()
        faculty_serializer=FacultySerializer(faculties,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)


@csrf_exempt
def faculty_details(request, id):
    try:
        faculties=Faculty.objects.get(id=id)
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        faculty_serializer=FacultySerializer(faculties)
        return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        faculties.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(faculties,data=mydict)
        if (faculty_serialize.is_valid()):
            faculty_serialize.save()
            return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        


@csrf_exempt
def searchapi(request):
    try:
        getcode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getcode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        return render(request,"searchfaculty.html",{"data":faculty_serializer.data})
        return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
    
    except Faculty.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")



@csrf_exempt
def updatesearchapi(request):
    try:
        getcode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getcode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        return render(request,"updatefaculty.html",{"data":faculty_serializer.data})
        return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Faculty.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def updatedataread(request):
    getnewid=request.POST.get("newid")
    getnewname=request.POST.get("newname")
    getnewcode=request.POST.get("newcode")
    getnewadd=request.POST.get("newadd")
    getnewmob=request.POST.get("newmob")
    getnewdepart=request.POST.get("newdepart")

    mydata={'id':getnewid,'name':getnewname,'fcode':getnewcode,'address':getnewadd,'mobnum':getnewmob,'department':getnewdepart}
    jsondata=json.dumps(mydata)
    apilink="http://127.0.0.1:8000/faculty/viewone/" + getnewid
    requests.put(apilink,data=jsondata)
    return HttpResponse("data updated successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getcode=request.POST.get("fcode")
        getfaculty=Faculty.objects.filter(fcode=getcode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        return render(request,"deletefaculty.html",{"data":faculty_serializer.data})
        return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Faculty.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def deletedataread(request):
    getnewid=request.POST.get("newid")

    apilink="http://127.0.0.1:8000/faculty/viewone/" + getnewid
    requests.delete(apilink)
    return HttpResponse("data deleted successfully")



