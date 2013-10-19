from django.db import models
import datetime

# Create your models here.
class Filling(models.Model):
    timestamp = models.DateTimeField('button pressed')
    
class LogEntry(models.Model):
    timestamp = models.DateTimeField('datapoint uploaded')
    ip = models.IPAddressField()
    rssi = models.IntegerField()
    humidity = models.FloatField()
    temp = models.FloatField()
    distance = models.IntegerField()
    millis = models.IntegerField()
