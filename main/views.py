from django.shortcuts import render

# Create your views here.
def mainpageview(request):
    return render(request ,"main.html") 