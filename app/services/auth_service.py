from rest_framework_simplejwt.tokens import RefreshToken
from app.serializers import RefreshTokenSerializer
from django.shortcuts import get_object_or_404
from app.models import Author


def generate_token(user):
    refresh_token = RefreshToken.for_user(user=user)
    serialzer = RefreshTokenSerializer(refresh_token)
    return serialzer.data


def get_current_user(id):
    return get_object_or_404(Author, id=id)
