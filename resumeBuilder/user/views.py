from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form_u = UserRegisterationForm(request.POST)
        print("hehe")
        if form_u.is_valid():
            print("haha")
            form_u.save()
            # messages.success(request, f'Your account has been created! You are now able to log in')
            messages.success(request,"Registered!!!!")
            return redirect('login')
       
    else:
        form_u = UserRegisterationForm()
    return render(request, 'user/register.html', {'form_u': form_u})

def profile(request):
    if request.method == "POST":
        form_u = UserUpdateForm(request.POST)
        form_p = ProfileUpdateForm(request.POST)
        print("post")
        if form_u.is_valid() and form_p.is_valid():
            print("haha")
            form_u.save()
            form_p.save()
            # messages.success(request, f'Your account has been created! You are now able to log in')
            messages.success(request,"Updated!!!!")
            return redirect('profile')
    else:
        form_u = UserUpdateForm(instance=request.user)
        form_p = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user/profile.html',{'form_u':form_u,'form_p':form_p})
