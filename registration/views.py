
from django.shortcuts import render,redirect
from .forms import preferenceform, profileform,UsercreateForm, userupdateform
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.views.generic import CreateView
# Create your views here.
def profilepage(request):
    if request.method=="POST":
        user_form= userupdateform(request.POST,instance=request.user)
        profile_form=profileform(request.POST,instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            return render(request,'home.html')
    else:
        user_form=userupdateform(instance=request.user)
        profile_form=profileform(instance=request.user.profile)
        
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
            
    else:
        user_form=UsercreateForm()       
    return render(request,'registeruser.html',{'form':user_form})        

