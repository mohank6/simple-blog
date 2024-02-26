from rest_framework_simplejwt.tokens import RefreshToken
from app.serializers import RefreshTokenSerializer


def generate_token(user):
    refresh_token = RefreshToken.for_user(user=user)
    serialzer = RefreshTokenSerializer(refresh_token)
    return serialzer.data
