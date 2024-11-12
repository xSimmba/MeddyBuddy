from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponse
from users.forms import LoginForm, UserRegistrationForm
from users.models import Profile
from mongoengine.errors import NotUniqueError
from users.auth_backend import MongoEngineBackend


def home(request):
    return render(request, "home.html")


def landing_page(request):
    if request.user.is_authenticated:
        return redirect("medication:home")
    return render(request, "landing-page.html")


def profile(request):
    return render(request, "profile.html")


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = Profile.objects.get(username=cd["username"])
                if user.check_password(cd["password"]):
                    if user.is_active:
                        MongoEngineBackend().authenticate(
                            request, username=cd["username"], password=cd["password"]
                        )
                        return redirect("users:landing_page")
                    else:
                        return HttpResponse("Disabled account")
                else:
                    return HttpResponse("Invalid login")
            except Profile.DoesNotExist:
                return HttpResponse("User does not exist")
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


# def register(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             new_user.set_password(form.cleaned_data["password"])
#             new_user.save()
#             Profile.objects.create(user=new_user)
#             return render(request, "landing-page.html")
#         else:
#             return HttpResponse("Invalid form")
#     else:
#         form = UserRegistrationForm()
#     return render(request, "registration/register.html", {"user_form": form})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            health_card = form.cleaned_data["health_card"]

            try:
                new_user = Profile(
                    username=username,
                    email=email,
                    health_card=health_card,
                    care_taker=False,
                )
                new_user.set_password(password)
                new_user.save()
                return render(request, "landing-page.html")
            except:
                return HttpResponse("Exception occurred")
        else:
            return HttpResponse("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"user_form": form})
