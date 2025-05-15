import datetime

from django.db import models
from django.utils import timezone



class Patient(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    register_date = models.DateTimeField('register date')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.first_name  + " " + self.last_name


class Arduino(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    arduino_id = models.CharField(max_length=12)    

    def __str__(self):
        return self.arduino_id


class ArduinoLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    arduino = models.ForeignKey(Arduino, on_delete=models.CASCADE)
    spo2 = models.FloatField()
    heart_rate = models.FloatField()
    log_date = models.DateTimeField('log date')

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name +  " - " + self.arduino.arduino_id