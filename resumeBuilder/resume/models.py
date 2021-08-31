from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.CharField(default="", max_length=50)

class BasicInformation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    first_name = models.CharField(default="", max_length=50)
    last_name = models.CharField(default="", max_length=50)
    email=models.EmailField()
    about = models.TextField(default="")
    contact = models.CharField(default="", max_length=15)
    address = models.TextField(default="")  
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    profession = models.CharField(max_length=200, default="")

    def ___str__(self):
        return self.resume
    

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    
    def ___str__(self):
        return self.resume

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    DEGREE_CHOICES = (
        ('Phd', 'Male'),
        ('Mtech/MA/MSc/MCom/MBA', 'Masters'),
        ('BE/Btech/BA/BSc/BCom', 'Masters'),
        ('12th', 'High School')
    )
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    stream = models.CharField(max_length=100)
    passing_year = models.DateField()
    result = models.CharField(max_length=5)

    def ___str__(self):
        return self.resume

class Skill(models.Model):
    LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advance', 'Advance'),
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_detail = models.TextField()
    skill_level = models.CharField(max_length=50, choices=LEVEL_CHOICES)

    def ___str__(self):
        return self.resume
    