from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.utils import timezone
from django.contrib import messages

from .forms import NewUserForm,RegisterDomainForm,SelectDomainForm,ChangePasswordForm
from .models import PageVisit, Domain
from django.contrib.auth.models import User

import requests
import json
import uuid
from ua_parser import user_agent_parser


def homepage(request):

	if request.user.is_authenticated:
		user = User.objects.get(id=request.session['_auth_user_id'])
		domains = [(d.id, d.domain_name) for d in Domain.objects.filter(user=user)]
		domains = sorted(domains)

		if request.method == "POST":
			select_domain_form = SelectDomainForm(data=request.POST, domains=domains)
			if select_domain_form.is_valid():
				domain = select_domain_form.cleaned_data.get('domain')
				page_visits = PageVisit.objects.filter(domain=domain).values().order_by("-time_opened")
				return render(request=request,
					template_name="pixel/home.html",
					context={"page_visits": page_visits, "domains":domains,"select_domain_form":select_domain_form})

		else:
			select_domain_form = SelectDomainForm(domains=domains)
			page_visits = PageVisit.objects.filter(domain=domains[0]).values().order_by("-time_opened")
			return render(request=request,
				template_name="pixel/home.html",
				context={"page_visits": page_visits, "domains":domains,"select_domain_form":select_domain_form})
	
	else:
		return render(request=request,
				template_name="pixel/home.html",)

	
def pixel(request, tracking_slug):
	
	tracking_slug = uuid.UUID(tracking_slug)
	tracking_slugs = [d.tracking_slug for d in Domain.objects.all()]
	if tracking_slug in tracking_slugs:
		domain = Domain.objects.get(tracking_slug=tracking_slug)
		#https://freegeoip.io/
		if 'HTTP_X_FORWARDED_FOR' in request.META.keys() and request.META['HTTP_X_FORWARDED_FOR'] is not None:
			ip = str(request.META['HTTP_X_FORWARDED_FOR'])
		elif 'REMOTE_ADDR' in request.META.keys():
			ip = str(request.META['REMOTE_ADDR'])
		else:
			ip = None

		if ip is not None:
			r = requests.get("https://freegeoip.app/json/" + ip)
			if r.status_code == 200:
				geoip = json.loads(r.text)
				ip = geoip['ip']
				country_code = geoip['country_code']
				country_name = geoip['country_name']
				region_name = geoip['region_name']
				#print("Time zone: " + geoip['time_zone'])

		if 'HTTP_USER_AGENT' in request.META.keys():
			ua_string = request.META.get('HTTP_USER_AGENT')

			os = user_agent_parser.ParseOS(ua_string)['family']
			agent = user_agent_parser.ParseUserAgent(ua_string)['family']
			device = user_agent_parser.ParseDevice(ua_string)['family']
		
		if 'HTTP_REFERER' in request.META.keys():
			print(request.META['HTTP_REFERER'])

		visit = PageVisit(domain=domain, ip=ip, agent=agent, os=os, device=device, country_name=country_name, country_code=country_code, region_name=region_name, time_opened=timezone.now())
		visit.save()
		return(HttpResponse('pixel'))


def settings(request):

	if request.user.is_authenticated:
		user = User.objects.get(id=request.session['_auth_user_id'])
		domains = [(d.id, d.domain_name) for d in Domain.objects.filter(user=user)]
		
		if request.method == "POST":
			register_domain_form = RegisterDomainForm(data=request.POST)
			delete_domain_form = SelectDomainForm(data=request.POST, domains=domains)
			change_password_form = ChangePasswordForm(data=request.POST,user=request.user)

			if register_domain_form.is_valid():
				domain_name = register_domain_form.cleaned_data.get("domain_name")
				domain = Domain(user=user,domain_name=domain_name)
				domain.save()
				domains = [(d.id, d.domain_name) for d in Domain.objects.filter(user=user)]
		
			elif delete_domain_form.is_valid():
				domain_id = delete_domain_form.cleaned_data.get("domain")
				Domain.objects.filter(id=domain_id).delete()
				domains = [(d.id, d.domain_name) for d in Domain.objects.filter(user=user)]
		
			elif change_password_form.is_valid():
				user = change_password_form.save()
				update_session_auth_hash(request, user)  # Important!
				return redirect("homepage")
			else:
				return HttpResponse("Not OK.")


			register_domain_form = RegisterDomainForm()
			delete_domain_form = SelectDomainForm(domains=domains)
			change_password_form = ChangePasswordForm(user=request.user)

			return render(request=request,
				template_name="pixel/settings.html",
				context = {"register_domain_form":register_domain_form,
				"delete_domain_form":delete_domain_form,
				"change_password_form":change_password_form})

		else:
			register_domain_form = RegisterDomainForm()
			delete_domain_form = SelectDomainForm(domains=domains)
			change_password_form = ChangePasswordForm(user=request.user)

			return render(request=request,
				template_name="pixel/settings.html",
				context = {"register_domain_form":register_domain_form,
				"delete_domain_form":delete_domain_form,
				"change_password_form":change_password_form})
	else:
		return redirect("homepage")


def register(request):
	
	if request.method == "POST":
		
		form = NewUserForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "New Account Created: {}.".format(username))
			login(request, user)
			messages.info(request, "You are now logged in as {}.".format(username))
			return redirect("homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, "{}:{}".format(msg,form.error_messages[msg]))	
	
	form = NewUserForm()
	return render(request,
				  "pixel/register.html",
				  context = {"form":form})


def login_req(request):

	if request.method == "POST":
		
		form = AuthenticationForm(request , data=request.POST  )
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				messages.info(request, "You are now logged in as {}.".format(username))
				return redirect("homepage")

			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()
	return render(request,
				  "pixel/login.html",
				  {"form":form})


def logout_req(request):
	
	if request.user.is_authenticated:
		logout(request)
		messages.info(request, "Logout Succesfully!")
		return redirect("homepage")
	else:
		messages.info(request, "You are not Logged In!")
		return redirect("homepage")