from turtle import home
from django.shortcuts import render,HttpResponse

# Create your views here.
def homepageview(request):
    return render(request ,'base.html') 