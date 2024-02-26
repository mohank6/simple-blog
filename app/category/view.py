from .category import Category
from .serializer import CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from app.api import ResponseBuilder, api
from app.services import auth_service


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_categories(request):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin':
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        categories = Category.get_all_categories()
        serializer = CategorySerializer(categories, many=True)
        return response_builder.get_200_success_response(
            message="Categories fetched", result=serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.CATEGORY_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_category_by_id(request, id):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin':
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        category = Category.get_category_by_id(id)
        serializer = CategorySerializer(category)
        return response_builder.get_200_success_response(
            message="Category fetched", result=serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.CATEGORY_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_category_by_name(request, name):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin':
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        category = Category.get_category_by_name(name)
        serializer = CategorySerializer(category)
        return response_builder.get_200_success_response(
            message="Category fetched", result=serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.CATEGORY_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin':
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_success_response(
                message="Category created", result=serializer.data
            )
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_category(request, id):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin':
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        is_PATCH = request.method == 'PATCH'
        category = Category.get_category_by_id(id)
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data, partial=is_PATCH)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_success_response(
                message="Category updated", result=serializer.data
            )
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_category(request, id):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin':
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        category = Category.get_category_by_id(id)
        Category.delete_category(id)
        return response_builder.get_204_no_content_response(message="Category deleted")
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.CATEGORY_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )
