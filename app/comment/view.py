from .comment import Comment
from .serializer import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.api import ResponseBuilder, api
from app.shared import paginate


@api_view(['GET'])
@csrf_exempt
def get_all_comments(request):
    response_builder = ResponseBuilder()
    try:
        comments = Comment.get_all_comments()
        paginated_comments, page_info = paginate(comments, request)
        serializer = CommentSerializer(paginated_comments, many=True)
        return response_builder.get_200_success_response(
            "Comments fetched successfully.", serializer.data, page_info
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.COMMENT_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@csrf_exempt
def get_comment_by_id(request, id):
    response_builder = ResponseBuilder()
    try:
        comment = Comment.get_comment_by_id(id)
        serializer = CommentSerializer(comment)
        return response_builder.get_200_success_response(
            "Comment fetched successfully.", serializer.data
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.COMMENT_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['GET'])
@csrf_exempt
def get_all_comments_of_post(request, id):
    response_builder = ResponseBuilder()
    try:
        comments = Comment.get_all_comments()
        paginated_comments, page_info = paginate(comments, request)
        serializer = CommentSerializer(paginated_comments, many=True)
        return response_builder.get_200_success_response(
            "Comments fetched successfully.", serializer.data, page_info
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.COMMENT_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['POST'])
@csrf_exempt
def create_comment(request):
    response_builder = ResponseBuilder()
    try:
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_success_response(
                "Comment created successfully.", serializer.data
            )
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.COMMENT_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['PUT', 'PATCH'])
@csrf_exempt
def update_comment(request, id):
    response_builder = ResponseBuilder()
    try:
        is_PATCH = request.method == 'PATCH'
        comment = Comment.get_comment_by_id(id)
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data=data, partial=is_PATCH)
        if serializer.is_valid():
            serializer.save()
            return response_builder.get_201_success_response(
                "Comment updated successfully.", serializer.data
            )
        return response_builder.get_400_bad_request_response(
            error_code=api.INVALID_INPUT, errors=serializer.errors
        )
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.COMMENT_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )


@api_view(['DELETE'])
@csrf_exempt
def delete_comment(request, id):
    response_builder = ResponseBuilder()
    try:
        comment = Comment.delete_comment(id)
        return response_builder.get_204_no_content_response(message="Comment deleted.")
    except ValueError as e:
        return response_builder.get_404_not_found_response(
            error_code=api.COMMENT_NOT_FOUND
        )
    except Exception as e:
        return response_builder.get_500_internal_server_error_response(
            error_code=api.INTERNAL_SERVER_ERROR, errors=str(e)
        )
