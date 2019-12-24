from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Domain
import uuid

class RegisterDomainForm(forms.Form):
    
	domain_name = forms.CharField(label='Domain Name', max_length=100)
	class Meta:
		model = Domain
		fields = ("username","domain_name","tracking_slug")


class DeleteDomainForm(forms.Form):
    
	CHOICES = (('Domain 1', 'domain 1'),('Domain 2', 'domain 2'),)
	domains = forms.ChoiceField(choices=CHOICES)
	
	class Meta:
		model = Domain


class ChangePasswordForm(PasswordChangeForm):
    
	class Meta:
		model = User
		fields = ("password","new_password","confirm")


class NewUserForm(UserCreationForm):
	
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = ("username","email","password1","password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user