from .comment import Comment
from .serializer import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
@csrf_exempt
def get_all_comments(request):
    try:
        comments = Comment.get_all_comments()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(
            {'message': 'No comments found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@csrf_exempt
def get_comment_by_id(request, id):
    try:
        comment = Comment.get_comment_by_id(id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(
            {'message': 'No comment found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@csrf_exempt
def get_all_comments_of_post(request, id):
    try:
        comments = Comment.get_all_comments_of_post(id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(
            {'message': 'No post or comments found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@csrf_exempt
def create_comment(request):
    try:
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response({'message': 'No post found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT', 'PATCH'])
@csrf_exempt
def update_comment(request, id):
    try:
        is_PATCH = request.method == 'PATCH'
        comment = Comment.get_comment_by_id(id)
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data=data, partial=is_PATCH)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response({'message': 'No post found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@csrf_exempt
def delete_comment(request, id):
    try:
        comment = Comment.delete_comment(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        return Response({'message': 'No post found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
