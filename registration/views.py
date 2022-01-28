
from email import message
from django.shortcuts import render,redirect
from .forms import preferenceform, profileform,UsercreateForm, userupdateform
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.views.generic import CreateView
<<<<<<< HEAD
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
=======
from django.contrib import messages 
>>>>>>> 13ec14dca54e8d98e613129bfd730f8aacba36d3
# Create your views here.




def profilepage(request):
    if request.method=="POST":
        user_form= userupdateform(request.POST,instance=request.user)
        profile_form=profileform(request.POST,instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            messages.success(request,f'Profile created successfully!!')
            return render(request,'home.html')
    else:
        user_form=userupdateform(instance=request.user)
        profile_form=profileform(instance=request.user.profile)
        messages.error(request, f'There seems to be an error in the form')
        
    return render(request,'profile.html', {'form':user_form,'p_form':profile_form}) 


def accountsetting(request):
    if request.method=="POST":
       form=userupdateform(request.POST,instance=request.user)
       profile_form=profileform(request.POST,request.FILES)
       preferences= preferenceform(request.POST)
       if form.is_valid() and profile_form.is_valid() and preferences.is_valid():
             form.save()
             profile_form.save()
             preferences.save()
             return  redirect('RUP')         
    else:
        form=userupdateform(instance=request.user)
        profile_form=profileform(instance=request.user.profile)
        preferences=preferenceform(request.POST)
    return render(request, 'preferencesinfo.html',{'f':form,'p':profile_form,'prefer':preferences})    



def registerpage(request):
    if request.method=="POST":
        user_form=UsercreateForm(request.POST)
        if user_form.is_valid():
            user_form.save() 
            messages.sucess(request,"Registration sucessfull.")          
            return redirect('login')
        else:
            messages.error(request,"unsucessful registration invalid information")    
            
     

        if  user_form.is_valid() :
            user_form.save()
            u_name = user_form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {u_name} !!')
            return redirect('login')

        
        

        
        

    else:
        user_form=UsercreateForm()       
    return render(request,'registeruser.html',{'form':user_form})        

