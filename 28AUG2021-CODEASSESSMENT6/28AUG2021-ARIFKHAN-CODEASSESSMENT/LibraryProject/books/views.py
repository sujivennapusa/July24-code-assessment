from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

def registerbook(request):
    return render(request,'register1.html')

def bookviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/books/viewall/").json
    return render(request,'view1.html',{"data":fetchdata})

def booksearch(request):
    return render(request,'search1.html')

def bookupdate(request):
    return render(request,'update1.html')

@csrf_exempt
def searchapi(request):
    try:
        getbookname=request.POST.get("bookname")
        getbook=Book.objects.filter(bookname=getbookname)
        book_serializer=BookSerializer(getbook,many=True)
        
        return render(request,"search1.html",{"data":book_serializer.data})
    except Book.DoesNotExist:
        return HttpResponse("Invalid bookname")
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def addbook(request):
    if (request.method=="POST"):
        
        getname=request.POST.get('bookname')
        getauthor=request.POST.get('author')
        getdescription=request.POST.get('description')
        getprice=request.POST.get('price')
        getcategory=request.POST.get('category')
        mydata={'bookname':getname,'author':getauthor,'description':getdescription,'price':getprice,'category':getcategory}

        # mydata=JSONParser().parse(request)
        book_serialize=BookSerializer(data=mydata)
        
        if (book_serialize.is_valid()):
            book_serialize.save()
            return redirect(bookviewss)
            # return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def book_all(request):
    if(request.method=="GET"):
        k=Book.objects.all()
        book_serializer=BookSerializer(k,many=True)
        return JsonResponse(book_serializer.data,safe=False)

@csrf_exempt
def book_single(request,fetchid):
    
    sh=Book.objects.get(id=fetchid)

    
    if(request.method=="GET"):
        book_serialize=BookSerializer(sh)
        return JsonResponse(book_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        book_serialize=BookSerializer(sh,data=mydata)

        if(book_serialize.is_valid()):
            book_serialize.save()
            return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(book_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def updatesearchapi(request):
    try:
        getbookname=request.POST.get("bookname")
        getbook=Book.objects.filter(bookname=getbookname)
        book_serializer=BookSerializer(getbook,many=True)

        return render(request,"update1.html",{"data":book_serializer.data})
    except Book.DoesNotExist:
        return HttpResponse("Invalid bookname")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def update_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getbookname=request.POST.get('newbookname')
        getauthor=request.POST.get('newauthor')
        getdescription=request.POST.get('newdescription')
        getprice=int(request.POST.get('newprice'))
        getcategory=request.POST.get("newcategory")
        mydata={'bookname':getbookname,'author':getauthor,'description':getdescription,'price':getprice,'category':getcategory}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/books/view/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

def bookdelete(request):
    return render(request,'delete1.html')

@csrf_exempt
def deletesearchapi(request):
    try:
        getbookname=request.POST.get("bookname")
        getbook=Book.objects.filter(bookname=getbookname)
        book_serializer=BookSerializer(getflat,many=True)
        return render(request,"delete1.html",{"data":book_serializer.data})
    except Book.DoesNotExist:
        return HttpResponse("Invalid bookname")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def delete_data_read(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/books/view/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")