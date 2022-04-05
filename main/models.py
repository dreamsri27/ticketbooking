from django.db import models

# Create your models here.

class user_DB(models.Model):
    name = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    phone_number =models.CharField(max_length=11)
    email = models.CharField(max_length=1000)


class events_DB(models.Model):
    name = models.CharField(max_length=1000)
    desc = models.TextField()
    venue = models.CharField(max_length=1000)
    
   

class booked_DB(models.Model):
    username = models.CharField(max_length=1000)
    event_name = models.CharField(max_length=100)


