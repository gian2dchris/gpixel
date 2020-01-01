from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
import uuid

# Create your models here.
class Domain(models.Model):
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User", on_delete=models.CASCADE)
	domain_name = models.CharField(max_length=200)
	tracking_slug = models.UUIDField(default=uuid.uuid4, editable=False)

	def __str__(self):
		return self.domain_name


class PageVisit(models.Model):
	
	ip = models.CharField(max_length=200)
	agent = models.CharField(max_length=200)
	os = models.CharField(max_length=200)
	device = models.CharField(max_length=200)
	country_name = models.CharField(max_length=200)
	country_code = models.CharField(max_length=200)
	region_name = models.CharField(max_length=200)
	time_opened = models.DateTimeField('time_opened')
	domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

	def __str__(self):
		return self.ip + self.time_opened
