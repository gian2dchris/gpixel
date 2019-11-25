from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class PageVisit(models.Model):
	
	ip = models.CharField(max_length=200)
	agent = models.CharField(max_length=200)
	os = models.CharField(max_length=200)
	device = models.CharField(max_length=200)
	country_name = models.CharField(max_length=200)
	country_code = models.CharField(max_length=200)
	region_name = models.CharField(max_length=200)
	time_opened = models.DateTimeField('time_opened')
