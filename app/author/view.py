from .author import Author
from .serializer import AuthorSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from app.api import ResponseBuilder, api
from app.services import auth_service
from app.shared import paginate
import logging


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_authors(request):
    logging.info('Get request on /api/v1/authors/')
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin':
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        authors = Author.get_all_authors()
        paginated_authors, page_info = paginate(authors, request)
        serializer = AuthorSerializer(paginated_authors, many=True)
        return response_builder.get_200_success_response(
            "Authors fetched successfully.", serializer.data, page_info
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.AUTHOR_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_author_by_id(request, id):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin' and not user.id == id:
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        author = Author.get_author_by_id(id)
        serializer = AuthorSerializer(author)
        return response_builder.get_200_success_response(
            "Author fetched successfully.", serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.AUTHOR_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_author(request):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin':
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        query = request.query_params.get('q', '')
        authors = Author.search_author(query)
        serializer = AuthorSerializer(authors, many=True)
        return response_builder.get_200_success_response(
            "Author fetched successfully.", serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.AUTHOR_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_author(request, id):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin' and not user.id == id:
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        data = JSONParser().parse(request)
        is_PATCH = request.method == 'PATCH'
        author = Author.get_author_by_id(id)
        serializer = AuthorSerializer(author, data=data, partial=is_PATCH)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_success_response(
                "Author updated successfully.", serializer.data
            )
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.AUTHOR_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_author(request, id):
    response_builder = ResponseBuilder()
    try:
        user = auth_service.get_current_user(request.user.id)
        if not user.role == 'admin' and not user.id == id:
            return response_builder.get_401_user_unauthorized(
                error_code=api.UNAUTHORIZED
            )
        author = Author.get_author_by_id(id)
        Author.delete_author(id)
        return response_builder.get_204_no_content_response(message="Author deleted")
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.AUTHOR_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )
