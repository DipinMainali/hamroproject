from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from destination.views import destination_view
from .forms import loginform
# Create your views here.

def loginpage(request):
    if request.method=="POST":
        #check either user exist or not
        login_form=loginform(request.POST)
        if login_form.is_valid():
         un=login_form.cleaned_data.get('username')
         pwd=login_form.cleaned_data.get('password')
         user=authenticate(request,username=un,password=pwd)
         if user is not None:
            login(request,user)
            return redirect('')

    else:
        login_form=loginform()
    return render(request,'login.html',{'form':login_form})

def logoutpage(request):
      logout(request)
      return redirect('login')



    

    

