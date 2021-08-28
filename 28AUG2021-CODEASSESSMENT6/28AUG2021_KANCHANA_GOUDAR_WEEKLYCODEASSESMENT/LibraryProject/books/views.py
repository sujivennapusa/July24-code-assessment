from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from rest_framework import status
from books.serialize import BookSerialize
from books.models import Books
import requests
def Addbook(request):
    return render(request,'Addbook.html')
def Viewallbook(request):
    fetchdata=requests.get("http://127.0.0.1:8000/books/viewallapi/").json()
    return render(request,'viewsbook.html',{"data":fetchdata})
def Searchbook(request):
    return render(request,'searchbook.html')
def Updatebook(request):
    return render(request,'updatebook.html')
def Deletebook(request):
    return render(request,'deletebook.html')


@csrf_exempt
def Bookadd(request):
    if(request.method=="POST"):
            # mydata=JSONParser().parse(request)
            book_serialize=BookSerialize(data=request.POST)
            if (book_serialize.is_valid()):
                book_serialize.save()
                return redirect(Viewallbook)
            else:
                return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)

def Bookviewall(request):
    if (request.method=="GET"):
        books=Books.objects.all()
        books_serialize=BookSerialize(books,many=True)
        return JsonResponse(books_serialize.data,safe=False)

@csrf_exempt
def Bookview(request,fetchid):
    try:
        books=Books.objects.get(id=fetchid)
    except Books.DoesNotExist:
        return HttpResponse("Invalid Book Id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        book_serializer=BookSerialize(books)
        return JsonResponse(book_serializer.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=="DELETE"):
        books.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if (request.method=="PUT"):
         mydata=JSONParser().parse(request)
         book_serialize=BookSerialize(books,data=mydata)
         if (book_serialize.is_valid()):
             book_serialize.save()
             return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)
         else:
              return JsonResponse(book_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def searchapi(request):
    try:
        getbname=request.POST.get("Bname")
        getb=Books.objects.filter(Bname=getbname)
        book_s=BookSerialize(getb,many=True)
        return render(request,"searchbook.html",{"data":book_s.data})
       
    except Book.DoesNotExist:
        return HttpResponse("Invalid book id",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update_searchapi(request):
    try:
        getbname=request.POST.get("Bname")
        getb=Books.objects.filter(Bname=getbname)
        book_s=BookSerialize(getb,many=True)
        return render(request,"updatebook.html",{"data":book_s.data})
       
    except Book.DoesNotExist:
        return HttpResponse("Invalid book id",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    print(getId)
    getname=request.POST.get("newBname")
    print(getname)
    getaut=request.POST.get("newAuthor")
    print(getaut)
    getdes=request.POST.get("newDes")
    print(getdes)
    getprice=request.POST.get("newPrice")
    print(getprice)
    getcat=request.POST.get("newCategory")
    print(getcat)
    mydata={"Bname":getname,"Author": getaut,"Des":getdes,"Price":getprice,"Category":getcat}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/books/viewapi/"+ getId
    requests.put(ApiLink,data=jsondata)
    return redirect(Viewallbook)

@csrf_exempt
def delete_searchapi(request):
    try:
        getbname=request.POST.get("Bname")
        getb=Books.objects.filter(Bname=getbname)
        book_s=BookSerialize(getb,many=True)
        return render(request,"deletebook.html",{"data":book_s.data})
       
    except Book.DoesNotExist:
        return HttpResponse("Invalid book id",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")


@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/books/viewapi/"+ getId
    requests.delete(ApiLink)
    return redirect(Viewallbook)