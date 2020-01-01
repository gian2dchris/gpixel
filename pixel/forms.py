from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Domain

import uuid

class RegisterDomainForm(forms.Form):

	domain_name = forms.CharField(label='Domain Name', max_length=100)
	
	class Meta:
		model = Domain
		fields = ("domain_name")


class SelectDomainForm(forms.Form):

	def __init__(self, *args, **kwargs):
		domains = kwargs.pop("domains")
		super(SelectDomainForm, self).__init__(*args, **kwargs)
		self.fields['domain'] = forms.ChoiceField(label='Domain Name', choices=domains)
	
	class Meta:
		model = Domain
		fields = ("domain")


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