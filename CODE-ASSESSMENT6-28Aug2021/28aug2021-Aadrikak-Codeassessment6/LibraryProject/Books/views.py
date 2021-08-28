from django.shortcuts import render
from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from Books.serializers import BookSerializer
from Books.models import Book
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

#####################################

@csrf_exempt
def addbook(request):
    if(request.method=="POST"):
        bookserial=BookSerializer(data=request.POST)
        if (bookserial.is_valid()):
            bookserial.save() 
            return response.JsonResponse(bookserial.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization")
    
def register(request):
    return render(request,'register.html')

#################################################################

@csrf_exempt
def viewbook(request):
    if (request.method=='GET'):
        book=Book.objects.all()
        bookserial=BookSerializer(book,many=True)
        return response.JsonResponse(bookserial.data, safe=False)

def bookview(request):
    fetch=requests.get("http://127.0.0.1:8000/books/viewbook/").json()
    return render(request,'viewbook.html',{"data":fetch})

#################################################################

@csrf_exempt
def viewbookdetails(request,id):
    try:
        book=Book.objects.get(id=id)
        if (request.method=='GET'):
            bookserial=BookSerializer(book) 
            return response.JsonResponse(bookserial.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            book.delete()
            return HttpResponse("deleted book")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            bookserial=BookSerializer(book,data=mydata)
            if (bookserial.is_valid()):
                bookserial.save()
                return response.JsonResponse(bookserial.data,status=status.HTTP_200_OK)
    except book.DoesNotExist:
        return HttpResponse("invalid ID ")
#############################################################


def searchbook(request):
    return render(request,'search.html')

@csrf_exempt
def searchapi(request):
    try:
        getbooknname=request.POST.get("bname")
        getbook=Book.objects.filter(bname=getbooknname)
        bookserial=BookSerializer(getbook,many=True)
       
        return render(request,"search.html",{"data":bookserial.data})
    except Book.DoesNotExist:
        return HttpResponse("invalid bookname")
    except:
        return HttpResponse("not runned")

############################################################
def update(request):
    return render(request,'update.html')

@csrf_exempt
def updatesearchapi(request):
    try:
        getnewname=request.POST.get("bname")
        getbook=Book.objects.filter( bname=getnewname)
        bookserial=BookSerializer(getbook,many=True)
        
        return render(request,"update.html",{"data":bookserial.data})
    except Book.DoesNotExist:
        return HttpResponse("Invalid book")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getnewname=request.POST.get('newbname')
        getnewbauthor=request.POST.get('newbauthor')
        getnewdescp=request.POST.get('newbdescp')
        getnewprice=request.POST.get('newbprice')
        getnewcat=request.POST.get('newbcategory')
        mydata={'bname':getnewname,'bauthor':getnewbauthor,'bdescp':getnewdescp,'bprice':getnewprice,'bcategory':getnewcat}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/books/viewbookdetails/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

#########################################################
def delete(request):
    return render(request,'delete.html')


@csrf_exempt
def deletesearchapi(request):
    try:
        getname=request.POST.get("bname")
        getbook=Book.objects.filter( bname=getname)
        bookserial=BookSerializer(getbook,many=True)
        # return JsonResponse(bookserial.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"delete.html",{"data":bookserial.data})
    except Book.DoesNotExist:
        return HttpResponse("Invalid book")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/books/viewbookdetails/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")

