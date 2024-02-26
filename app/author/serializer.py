from rest_framework import serializers
from app.models import Author
from django.contrib.auth.password_validation import validate_password


class AuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio', 'created_at', 'password', 'role']

    def validate_password(self, value):
        validate_password(value)
        return value


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
