from django.db import models
from datetime import date


# Create your models here.
class History(models.Model):
    collect_date = models.DateField(auto_now_add=True)
    sensor_low = models.CharField(max_length=30)
    sensor_mid = models.CharField(max_length=30)
    sensor_high = models.CharField(max_length=30)
    sensor_floor = models.CharField(max_length=30)
  

class Cleaning(models.Model):
	collect_date = models.DateField(default=date.today)
	state_of_success  = models.BooleanField()
	time_of_cleaning = models.CharField(max_length=30) 
