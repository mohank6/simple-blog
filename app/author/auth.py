from .author import Author
from .serializer import (
    AuthorSerializer,
    LoginSerializer,
    OtpSerializer,
    ResetPasswordSerializer,
)
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.api import ResponseBuilder, api


@api_view(['POST'])
@csrf_exempt
def signup(request):
    try:
        response_builder = ResponseBuilder()
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            Author.generate_and_send_otp(serializer.validated_data['email'])
            return response_builder.get_201_success_response(
                "Please verify your email", serializer.data
            )
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['POST'])
@csrf_exempt
def login(request):
    try:
        response_builder = ResponseBuilder()
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            email, password = (
                serializer.validated_data['email'],
                serializer.validated_data['password'],
            )
            author, token = Author.login(email, password)
            return response_builder.get_200_logged_in(author, token)
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except ValueError as e:
        return response_builder.get_401_user_unauthorized(
            error_code=api.INVALID_CREDENTIALS, errors=str(e)
        )

    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['POST'])
@csrf_exempt
def verify_email(request):
    try:
        response_builder = ResponseBuilder()
        serializer = OtpSerializer(data=request.POST)
        if serializer.is_valid():
            email, otp = (
                serializer.validated_data['email'],
                serializer.validated_data['otp'],
            )
            author = Author.verify_email(email, otp)
            author_serializer = AuthorSerializer(author)
            return response_builder.get_200_success_response(author)
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except ValueError as e:
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_OTP, errors=str(e)
        )

    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['POST'])
@csrf_exempt
def forgot_password(request):
    try:
        response_builder = ResponseBuilder()
        email = request.data.get('email')
        Author.generate_and_send_otp(email=email)
        return response_builder.get_200_success_response(
            message='OTP sent to email', result={}
        )
    except ValueError as e:
        return response_builder.get_400_bad_request_response(
            error_code=api.AUTHOR_NOT_FOUND, errors=str(e)
        )

    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['POST'])
@csrf_exempt
def reset_password(request):
    try:
        response_builder = ResponseBuilder()
        serializer = ResetPasswordSerializer(data=request.POST)
        if serializer.is_valid():
            email, otp, password = (
                serializer.validated_data['email'],
                serializer.validated_data['otp'],
                serializer.validated_data['password'],
            )
            Author.reset_password(email, otp, password)
            return response_builder.get_200_success_response(
                message='Password changed successfully.', result={}
            )
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except ValueError as e:
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=str(e)
        )

    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )
