from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model that extends the User model with additional user information.

    Attributes:
        id (OneToOneField): One-to-one relationship with the User model. Serves as the primary key.
        care_giver (BooleanField): Indicates if the user is a caregiver. Defaults to False.
        date_of_birth (DateField): The user's date of birth. Can be blank or null.
        email (EmailField): The user's email address. Can be blank or null.
        health_card (CharField): The user's health card information. Maximum length of 2000 characters. Can be blank or null.
    """

    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=100, unique=False)
    care_giver = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    health_card = models.CharField(max_length=2000, blank=True, null=True)
