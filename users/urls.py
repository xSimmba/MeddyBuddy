from django.urls import path
from .views import user_login, user_logout, register, profile, landing_page

app_name = "users"

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
