from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import Profile
from .models import *

# Create your views here.
def home(request):
    return render(request,'resume/home.html')

def testing(request):
    return render(request, 'resume_templates/template3.html')

@login_required
def forms(request):
    
    return render(request,'resume/forms.html')