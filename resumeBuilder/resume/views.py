from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import Profile
from django.views.decorators.clickjacking import xframe_options_exempt
import json
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'resume/home.html')


@xframe_options_exempt
def testing(request):
    return render(request, 'resume_templates/template3.html')

@login_required
def forms(request):
   
    if request.method == 'POST':
        education = request.POST.get('education',"Education not found")
        print(education)
        job = request.POST.get('job','Job not found')
        print(job)
        skill = request.POST.get('skill','Skill not found')
        print(skill)
        ctx = {}
        return HttpResponse(json.dumps(ctx), content_type='application/json')

    context = {
        'resume_template': 'resume_templates/template1.html'
    }
    return render(request,'resume/forms.html')