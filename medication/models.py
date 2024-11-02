from django.db import models

# Create your models here.
class Medication(models.Model):
    id = models.AutoField(primary_key=True)
    user_id  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dosage = models.IntegerField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    