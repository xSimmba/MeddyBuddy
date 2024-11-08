from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm


def home(request):
    return render(request, "home.html")


def landing_page(request):
    return render(request, "landing-page.html")


def profile(request):
    return render(request, "profile.html")


def user_login(request):
    """
    Handle user login functionality.

    This view handles both GET and POST requests for user login. If the request
    method is POST, it processes the login form data. If the form is valid, it
    authenticates the user with the provided username and password. If the user
    is authenticated and active, they are logged in and redirected to the home
    page. If the authentication fails, an "Invalid login" message is returned.
    If the request method is GET, an empty login form is rendered.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered login form or
                      a redirect to the home page if login is successful.
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("medication:home")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


def user_logout(request):
    """
    Logs out the user and renders the landing page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered landing page.
    """
    logout(request)
    return render(request, "landing-page.html")


def register(request):
    """
    Handle user registration.

    This view handles the registration of a new user. If the request method is POST,
    it processes the submitted registration form. If the form is valid, it creates
    a new user, sets the user's password, and saves the user to the database.
    It then renders the landing page. If the request method is not POST, it
    displays an empty registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration form page or the landing page
        upon successful registration.
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(request, "landing-page.html")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"user_form": form})
