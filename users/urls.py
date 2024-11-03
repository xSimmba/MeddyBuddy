from django.urls import path
<<<<<<< HEAD
from .views import user_login, user_logout, register
=======
from .views import user_login, user_logout, register, profile
from django.contrib.auth import views as auth_views
>>>>>>> 2edf5c9 (update: login functionality)

urlpatterns = [
    path("profile/", profile, name="profile"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
]