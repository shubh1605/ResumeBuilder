from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Widget
from .models import Profile
from django.db import transaction

jobChoices = (("Student", "Student"),("Doctor","Doctor"),("Engineer","Engineer"))

class UserRegisterationForm(UserCreationForm):
	phone_number = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	job = forms.CharField(required=True,widget=forms.Select(choices=jobChoices))
	
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'job',
				   'password1', 'password2']

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		user.save()
		profile = Profile.objects.create(user=user)
		profile.phoneNumber = self.cleaned_data.get('phone_number')
		profile.job = self.cleaned_data.get('job')
		profile.save()
		return user
