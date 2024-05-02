from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomToken

class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Token'

    def authenticate_credentials(self, key):
        try:
            token = CustomToken.objects.get(key=key)
        except CustomToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        user = token.user  # Assuming 'user' is an instance of your custom user model
        if not user.is_active:
            raise AuthenticationFailed('User inactive or deleted')

        return (user, token)

