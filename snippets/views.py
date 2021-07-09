from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from snippets import serializers
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer      
from django.contrib.auth.models import User 
from rest_framework.decorators import permission_classes
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def UserList(request, format=None):

    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True  )
        return Response(serializer.data)

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def snippet_list(request, format=None):
    
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def UserDetail(request, pk):
    try:
        user_detail = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':

        serializer = UserSerializer(user_detail)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user_detail, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user_detail.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, IsOwnerOrReadOnly,))
def snippet_detail(request,pk, format=None):
    
    try:
        snippet = Snippet.objects.get(pk=pk)

    except Snippet.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

