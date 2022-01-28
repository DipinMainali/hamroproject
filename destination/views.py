from django.shortcuts import render

# Create your views here.
def destination_view(request):
    return render(request,'destination.html')
