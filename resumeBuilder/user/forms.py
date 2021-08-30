from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Profile
from django.db import transaction

jobChoices = (("Student", "Student"),("Doctor","Doctor"),("Engineer","Engineer"))

class UserRegisterationForm(UserCreationForm):
	phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Phone number"}))
	# email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Email-Id"}))
	job = forms.CharField(required=True,widget=forms.Select(choices=jobChoices, attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Job"}))
	# username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control bg-white border-left-0 border-md",'placeholder':"Username"}))
	# 
	# last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Last Name"}))
	# password1 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Password"}))
	# password2 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Confirm Password"}))

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'job',
				   'password1', 'password2']

		widgets = {
			'username':  forms.TextInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Phone number"}),
			'first_name' : forms.TextInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"First Name"}),
			'last_name':forms.TextInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Last Name"}),
			'password1':forms.PasswordInput() ,
			# 'password1': forms.PasswordInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Password "}),
			'password2': forms.PasswordInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Confirmation Password "}),
			'email': forms.EmailInput(attrs={'class': "form-control bg-white border-left-0 border-md", 'placeholder':"Email"}),
		}

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
