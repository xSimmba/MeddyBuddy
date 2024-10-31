from django.db import models
from medication.models import Medication

# Create your models here.

class Reminder(models.Model):
    id = models.AutoField(primary_key=True)
    user_id  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medication_id  = models.ForeignKey(Medication , on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    user_id  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medication_id  = models.ForeignKey(Medication, on_delete=models.CASCADE)
    schedule_time = models.DateField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()