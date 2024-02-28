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

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            del validated_data['password']
        return super().update(instance, validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class OtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    otp = serializers.IntegerField()

    def validate_password(self, value):
        validate_password(value)
        return value
