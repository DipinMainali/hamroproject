
from email import message
from django.shortcuts import render,redirect
from .forms import profileform, UsercreateForm, userupdateform
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.views.generic import CreateView
from django.contrib import messages 
# Create your views here.
def profilepage(request):
    if request.method=="POST":
        user_form= userupdateform(request.POST,instance=request.user)
        profile_form=profileform(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            messages.success(request,'Account created successfully!!')
            return render(request,'home.html')
    else:
        user_form=userupdateform(instance=request.user)
        profile_form=profileform(instance=request.user.profile)
        
    return render(request,'profile.html', {'form':user_form,'p_form':profile_form}) 

def accountsetting(request):
    if request.method=="POST":
       form=userupdateform(request.POST,instance=request.user)
       profile_form=profileform(request.POST,request.FILES)
       if form.is_valid() and profile_form.is_valid():
           form.save()
           profile_form.save()
           return redirect('destination')
    else:
        form=userupdateform()
        profile_form=profileform()
    return render(request, 'preferencesinfo.html',{'f':form,'p':profile_form})    

def registerpage(request):
    if request.method=="POST":
        user_form=UsercreateForm(request.POST)
        if user_form.is_valid():
            pw1=user_form.cleaned_data.get('password1')
            pw2=user_form.cleaned_data.get('password2')
            if(pw1==pw2):
                user_form.save()           
                return redirect('login')
            else:
                messages.add_message(request, messages.INFO, 'Passwords did not match !!!!!!')
                return redirect('registerpage')
                

    else:
        user_form=UsercreateForm()       
    return render(request,'registeruser.html',{'form':user_form})        

