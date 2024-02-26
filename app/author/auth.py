from .author import Author
from .serializer import AuthorSerializer, LoginSerializer
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
            return response_builder.get_201_success_response(
                "Author created successfully.", serializer.data
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
            error_code=api.INVALID_CREDENTIALS
        )

    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )
