from .post import Post
from .serializer import PostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from app.api import ResponseBuilder, api


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_posts(request):
    response_builder = ResponseBuilder()
    try:
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
@permission_classes([IsAuthenticated])
def get_post_by_id(request, id):
    response_builder = ResponseBuilder()
    try:
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
@permission_classes([IsAuthenticated])
def get_posts_by_author(request, id):
    response_builder = ResponseBuilder()
    try:
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
@permission_classes([IsAuthenticated])
def get_posts_of_category(request, id):
    response_builder = ResponseBuilder()
    try:
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
@permission_classes([IsAuthenticated])
def create_post(request):
    response_builder = ResponseBuilder()
    try:
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
@permission_classes([IsAuthenticated])
def update_post(request, id):
    response_builder = ResponseBuilder()
    try:
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
@permission_classes([IsAuthenticated])
def delete_post(request, id):
    response_builder = ResponseBuilder()
    try:
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
