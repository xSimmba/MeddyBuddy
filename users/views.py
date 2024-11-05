from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "landing-page.html")


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return render(request, "landing-page.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(request, "registration/register_done.html")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"user_form": form})


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    user = get_object_or_404(User, username=request.user)
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(initial=model_to_dict(user))
    return render(request, "profile.html", {"user_form": user_form, "profile": profile})
