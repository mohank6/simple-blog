from .author import Author
from .serializer import AuthorSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
@csrf_exempt
def get_all_authors(request):
    try:
        authors = Author.get_all_authors()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(
            {'message': 'No authors found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@csrf_exempt
def get_author_by_id(request, id):
    try:
        author = Author.get_author_by_id(id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(
            {'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@csrf_exempt
def create_author(request):
    try:
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT', 'PATCH'])
@csrf_exempt
def update_author(request, id):
    try:
        data = JSONParser().parse(request)
        is_PATCH = request.method == 'PATCH'
        author = Author.get_author_by_id(id)
        serializer = AuthorSerializer(author, data=data, partial=is_PATCH)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response(
            {'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@csrf_exempt
def delete_author(request, id):
    try:
        author = Author.get_author_by_id(id)
        Author.delete_author(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        return Response(
            {'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
