from .post import Post
from .serializer import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError


@api_view(['GET'])
@csrf_exempt
def get_all_posts(request):
    try:
        posts = Post.get_all_posts()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({'message': 'No posts found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@csrf_exempt
def get_post_by_id(request, id):
    try:
        post = Post.get_post_by_id(id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({'message': 'No posts found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@csrf_exempt
def get_posts_by_author(request, id):
    try:
        posts = Post.get_posts_by_author(id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(
            {'message': 'Author or Posts not found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@csrf_exempt
def get_posts_of_category(request, id):
    try:
        posts = Post.get_posts_of_category(id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(
            {'message': 'Category or Posts not found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@csrf_exempt
def create_post(request):
    try:
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT', 'PATCH'])
@csrf_exempt
def update_post(request, id):
    try:
        is_PATCH = request.method == 'PATCH'
        post = Post.get_post_by_id(id)
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data, partial=is_PATCH)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return


@api_view(['DELETE'])
@csrf_exempt
def delete_post(request, id):
    try:
        Post.delete_post(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        return Response(
            {'message': 'Post does not exists'}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
