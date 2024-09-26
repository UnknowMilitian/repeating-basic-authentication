import base64
from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomBasicAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.headers.get("Authorization")

        if not auth or not auth.startswith("Basic "):
            return None

        try:
            auth_parts = base64.b64decode(auth.split(" ")[1]).decode("utf-8")
            username, password = auth_parts.split(":")
        except (TypeError, ValueError):
            raise AuthenticationFailed("Authentication details invalid")

        # Authenticate the user manually
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("No such user")

        # Check the password
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        print(f"Authenticated user: {user.username}")

        return (user, None)
