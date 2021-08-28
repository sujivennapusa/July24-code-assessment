from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from books.serializers import booksSerializer
from books.models import Books
from rest_framework.parsers import JSONParser 
from rest_framework import status
import requests
@csrf_exempt
def searchapi(request):
    try:
        getbookname=request.POST.get("book_name")
        getBookname=Books.objects.filter(book_name=getbookname)
        books_serializer=booksSerializer(getBookname,many=True)
        return render(request,"search.html",{"data":books_serializer.data})

    except:
        return HttpResponse("invalid Book Name")
@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    getbookname=request.POST.get("newbookname")
    getauthor=request.POST.get("newauthor")
    getdescription=request.POST.get("newdescription")
    getprice=request.POST.get("newprice")
    getcategory=request.POST.get("newcategory")
     
    mydata={"book_name":getbookname,"author":getauthor,"description":getdescription,"price":getprice,"category":getcategory}
    jsondata=json.dumps(mydata)
    ApiLink="http://localhost:8000/books/view/"+ getId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("data updated successfully")
@csrf_exempt 
def update_api(request):
    try:
        getbookname=request.POST.get("book_name")
        getBookname=Books.objects.filter(book_name=getbookname)
        books_serializer=booksSerializer(getBookname,many=True)
        return render(request,"update.html",{"data":books_serializer.data})

    except:
        return HttpResponse("invalid Book Name")
@csrf_exempt
def delete_data_read(request):
    getId=request.POST.get("newid")
    ApiLink="http://localhost:8000/books/view/"+ getId 
    requests.delete(ApiLink)
    return HttpResponse("data deleted successfully")
@csrf_exempt
def delete_api(request):
    try:
        getbookname=request.POST.get("book_name")
        getBookname=Books.objects.filter(book_name=getbookname)
        books_serializer=booksSerializer(getBookname,many=True)
        return render(request,"delete.html",{"data":books_serializer.data})
    except:
        return HttpResponse("invalid Book Name")
@csrf_exempt
def booksPage(request):
    if(request.method=="POST"):
    #    mydict=JSONParser().parse(request)   
       books_serialize=booksSerializer(data=request.POST)  
       if(books_serialize.is_valid()):
           books_serialize.save()
           return redirect(viewall)
       else:
           return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Httpresponse("No Get method allowed",status=status.HTTP_400_BAD-REQUEST)
@csrf_exempt
def books_list(request):
    if(request.method=="GET"):
        books=Books.objects.all()
        books_serializer=booksSerializer(books,many=True)
        return JsonResponse(books_serializer.data,safe=False)
@csrf_exempt
def books_details(request,fetchid):
    try:
        books=Books.objects.get(id=fetchid)
        if(request.method=="GET"):
            books_serializer=booksSerializer(books)
            return JsonResponse(books_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            books.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            books_serializer=booksSerializer(books,data=mydict)
            if(books_serializer.is_valid()):
                books_serializer.save()
                return JsonResponse(books_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(books_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Books.DoesNotExist:
        return HttpResponse("invalid books id",status=status.HTTP_404_NOT_FOUND)

def register(request):
    return render(request,'booksregister.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/books/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
def home_view(request):
    return render(request,'home.html')
def search_view(request):
    return render(request,'search.html')
def update_view(request):
    return render(request,'update.html')
def delete_view(request):
    return render(request,'delete.html')