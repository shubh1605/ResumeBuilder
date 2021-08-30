from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'resume/home.html')

def testing(request):
    return render(request, 'resume_templates/template3.html')