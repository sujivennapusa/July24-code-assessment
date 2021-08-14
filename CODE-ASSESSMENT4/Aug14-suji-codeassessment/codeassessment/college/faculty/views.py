from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def facultyAddPage(request):
    if request.method=="POST":
        getName=request.POST.get("name")
        getDept=request.POST.get("department")
        getCollege=request.POST.get("college")
        getAddress=request.POST.get("address")
        
        mydict={"name":getName,"address":getAddress,"college":getCollege,"department":getDept};
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("No get method allowed")