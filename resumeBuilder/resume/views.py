from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import Profile
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import *

# Create your views here.
def home(request):
    return render(request,'resume/home.html')


@xframe_options_exempt
def testing(request):
    return render(request, 'resume_templates/template3.html')

@login_required
def forms(request):
    context = {
        'resume_template': 'resume_templates/template1.html'
    }
    return render(request,'resume/forms.html')