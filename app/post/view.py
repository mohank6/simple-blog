from .post import Post
from .serializer import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError
from app.api import ResponseBuilder, api


@api_view(['GET'])
@csrf_exempt
def get_all_posts(request):
    try:
        response_builder = ResponseBuilder()
        posts = Post.get_all_posts()
        serializer = PostSerializer(posts, many=True)
        return response_builder.get_200_success_response(
            "Posts fetched successfully.", serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.POST_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@csrf_exempt
def get_post_by_id(request, id):
    try:
        response_builder = ResponseBuilder()
        post = Post.get_post_by_id(id)
        serializer = PostSerializer(post)
        return response_builder.get_200_success_response(
            "Post fetched successfully.", serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.POST_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@csrf_exempt
def get_posts_by_author(request, id):
    try:
        response_builder = ResponseBuilder()
        posts = Post.get_posts_by_author(id)
        serializer = PostSerializer(posts, many=True)
        return response_builder.get_200_success_response(
            "Post fetched successfully.", serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.POST_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@csrf_exempt
def get_posts_of_category(request, id):
    try:
        response_builder = ResponseBuilder()
        posts = Post.get_posts_of_category(id)
        serializer = PostSerializer(posts, many=True)
        return response_builder.get_200_success_response(
            "Post fetched successfully.", serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.POST_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['POST'])
@csrf_exempt
def create_post(request):
    try:
        response_builder = ResponseBuilder()
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_success_response(
                "Post created successfully.", serializer.data
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
def update_post(request, id):
    try:
        response_builder = ResponseBuilder()
        is_PATCH = request.method == 'PATCH'
        post = Post.get_post_by_id(id)
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data, partial=is_PATCH)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_success_response(
                "Post updated successfully.", serializer.data
            )
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.POST_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['DELETE'])
@csrf_exempt
def delete_post(request, id):
    try:
        response_builder = ResponseBuilder()
        Post.delete_post(id)
        return response_builder.get_204_no_content_response(message="Post deleted")
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.POST_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )
