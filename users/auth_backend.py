from django.contrib.auth.backends import BaseBackend
from django.shortcuts import redirect


class MongoEngineBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        from users.models import Profile

        try:
            user = Profile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Profile.DoesNotExist:
            return None

    def logout(self, request):
        from django.contrib.auth import logout

        logout(request)

    def get_user(self, user_id):
        from users.models import Profile

        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        from users.models import Profile

        try:
            user = Profile.objects.get(username=username)
            if user.check_password(password) and user.is_admin:
                return user
        except Profile.DoesNotExist:
            return None

    def logout(self, request):
        from django.contrib.auth import logout

        logout(request)
        return redirect('/admin/login/')

    def get_user(self, user_id):
        from users.models import Profile

        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None
