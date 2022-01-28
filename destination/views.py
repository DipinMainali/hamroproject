from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Places

# Create your views here.

def destination_view(request,pID):
    des=Places.objects.get(pID=pID)
    return render(request,'destination.html',{'obj':des})

