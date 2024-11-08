from django.db import models
from medication.models import Medication

# Create your models here.

class Reminder(models.Model):
    """
    Reminder model to store information about medication reminders for users.

    Attributes:
        id (AutoField): Primary key for the Reminder model.
        user_id (ForeignKey): Foreign key to the User model from the auth app.
        medication_id (ForeignKey): Foreign key to the Medication model.
        created_at (DateTimeField): Timestamp when the reminder was created.
        updated_at (DateTimeField): Timestamp when the reminder was last updated.
    """
    id = models.AutoField(primary_key=True)
    user_id  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medication_id  = models.ForeignKey(Medication , on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Schedule(models.Model):
    """
    Schedule model to store medication schedules for users.

    Attributes:
        id (AutoField): Primary key for the schedule.
        user_id (ForeignKey): Reference to the user who owns the schedule.
        medication_id (ForeignKey): Reference to the medication being scheduled.
        schedule_time (DateField): The date and time when the medication is scheduled.
        status (BooleanField): The status of the schedule (default is False).
        created_at (DateTimeField): The date and time when the schedule was created.
        updated_at (DateTimeField): The date and time when the schedule was last updated.
    """
    id = models.AutoField(primary_key=True)
    user_id  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    medication_id  = models.ForeignKey(Medication, on_delete=models.CASCADE)
    schedule_time = models.DateField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()