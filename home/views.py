from django.shortcuts import render,HttpResponse

# Create your views here.
def homepageview(request):
    return HttpResponse('this is homepage')