from django.shortcuts import render,HttpResponse
from destination.models import Places

# Create your views here.

def Home_notlog(request,pID):
    obj=Places.objects.get(pID=pID)
    
