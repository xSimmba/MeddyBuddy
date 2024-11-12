from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=100,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        max_length=100,
    )


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    health_card = forms.CharField(max_length=1000, required=False)
    date_of_birth = forms.DateField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput, required=True
    )

    def save(self):
        user = Profile(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            health_card=self.cleaned_data["health_card"],
            date_of_birth=self.cleaned_data["date_of_birth"],
        )
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]
