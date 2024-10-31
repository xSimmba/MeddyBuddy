from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)
    care_giver = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
