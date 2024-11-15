from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class LoginForm(forms.Form):
    """
    LoginForm is a Django form for user authentication.

    Fields:
        username (CharField): A text field for the username with a maximum length of 100 characters.
        password (CharField): A password field for the password with a maximum length of 100 characters.

    Both fields use Bootstrap's 'form-control' class for styling.
    """

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


class UserRegistrationForm(forms.ModelForm):
    """
    UserRegistrationForm is a Django ModelForm for user registration.

    Fields:
        password (CharField): A password input field with a form-control CSS class.
        password2 (CharField): A repeat password input field with a form-control CSS class.
        date_of_birth (DateField): A date input field for the user's date of birth with a form-control CSS class.
        health_card (CharField): A text input field for the user's health card with a form-control CSS class.

    Meta:
        model (User): The model associated with this form.
        fields (tuple): The fields to include in the form, specifically 'username' and 'email'.

    Methods:
        clean_password2(): Validates that the password and repeat password fields match. Raises a ValidationError if they do not.
    """

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )

    health_card = forms.CharField(
        label="Health Card",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        profile = Profile.objects.create(
            id=user,
            username=self.cleaned_data["username"],
            date_of_birth=self.cleaned_data["date_of_birth"],
            health_card=self.cleaned_data["health_card"],
        )
        profile.save()
        return user

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class IsCareGiverForm(forms.ModelForm):
    is_caregiver = forms.TypedChoiceField(
        label="Are you a caregiver?",
        choices=((True, "Yes"), (False, "No")),
        coerce=lambda x: x == "True",
        widget=forms.RadioSelect,
        required=True,
    )

    class Meta:
        model = Profile
        fields = ["care_giver"]
