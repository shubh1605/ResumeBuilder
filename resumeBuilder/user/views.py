from django.shortcuts import render
from .forms import UserRegisterationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Profile

def register(request):
    if request.method == 'POST':
        form_u = UserRegisterationForm(request.POST)
        if form_u.is_valid():
            form_u.save()
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('register')
    else:
        form_u = UserRegisterationForm()
    return render(request, 'user/register.html', {'form_u': form_u})
