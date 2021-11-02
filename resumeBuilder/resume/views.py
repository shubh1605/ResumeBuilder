from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import Profile
from django.views.decorators.clickjacking import xframe_options_exempt
import json
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    return render(request, 'resume/home.html')


@xframe_options_exempt
def testing(request):
    return render(request, 'resume_templates/template3.html')


@login_required
def forms(request):

    if request.method == 'POST':
        try:
            educations = json.loads(request.POST.get('education'))
            jobs = json.loads(request.POST.get('job')) 
            skills = json.loads(request.POST.get('skill'))      
            info = json.loads(request.POST.get('info'))
        except:
            print('HEHEHEHEHEH')
        # print(educations,jobs,skills,info)
        ctx = {}
        loggedUser = request.user
        resume = Resume(user=loggedUser, template="template 1")
        resume.save()
        basicInfo = BasicInformation(resume=resume, first_name=info[0][0], last_name=info[1][0], email=info[2][0], contact=info[3]
                                     [0], address=info[4][0], profession=info[5][0], github=info[6][0], linkedin=info[7][0], about=info[8][0])
        
        for education in educations:
            new_education = Education(resume = resume, degree = education[0], branch = education[1], university = education[2], passing_year = education[3], result = education[4])
            new_education.save()

        for job in jobs:
            new_job = Experience(resume=resume, job_title = job[0], employer = job[1], start_date = job[2], end_date =job[3], description = job[4])
            new_job.save()


        for skill in skills:
            new_skill = Skill(resume=resume, skill_detail= skill[0], skill_level = skill[1])
            new_skill.save()

        basicInfo.save()

        return HttpResponse(json.dumps(ctx), content_type='application/json')

    context = {
        'resume_template': 'resume_templates/template1.html',
        'user' : request.user,
    }
    return render(request, 'resume/forms.html')
