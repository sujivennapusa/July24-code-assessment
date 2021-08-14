from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def studentAddPage(request):
    if request.method=="POST":
        getName=request.POST.get("name")
        getRollno=int(request.POST.get("rollno"))
        getCollege=request.POST.get("college")
        getAdmino=int(request.POST.get("admino"))
        getParent=request.POST.get("parent")
        mydict={"name":getName,"rollno":getRollno,"college":getCollege,"parent":getParent,"admino":getAdmino};
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("No get method allowed")