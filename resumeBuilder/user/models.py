from django.db import models
from django.contrib.auth.models import User

jobChoices = (("Student", "Student"),("Doctor","Doctor"),("Engineer","Engineer"))

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	job = models.CharField(max_length = 20,choices=jobChoices,default='Student')
	phoneNumber = models.CharField(max_length=10)

	def ___str__(self):
		return self.user.username
	