from .author import Author
from .serializer import AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.api import ResponseBuilder, api


@api_view(['GET'])
@csrf_exempt
def get_all_authors(request):
    try:
        response_builder = ResponseBuilder()
        authors = Author.get_all_authors()
        serializer = AuthorSerializer(authors, many=True)
        return response_builder.get_200_success_response(
            "Authors fetched successfully.", serializer.data
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
@csrf_exempt
def get_author_by_id(request, id):
    try:
        response_builder = ResponseBuilder()
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


@api_view(['POST'])
@csrf_exempt
def create_author(request):
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


@api_view(['PUT', 'PATCH'])
@csrf_exempt
def update_author(request, id):
    try:
        response_builder = ResponseBuilder()
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
@csrf_exempt
def delete_author(request, id):
    try:
        response_builder = ResponseBuilder()
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
