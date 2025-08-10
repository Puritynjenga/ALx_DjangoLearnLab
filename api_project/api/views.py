from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class BookList(generics.ListAPIView):
    # This view will handle listing all books
    # It will use the BookSerializer to serialize the data
    # It will also require authentication using TokenAuthentication 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer   

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # This viewset will handle all CRUD operations for the Book model
    # It will automatically provide list, create, retrieve, update, and destroy actions
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomAuthToken(ObtainAuthToken):
    """
    Custom authentication view to return the token in the response.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key, 
            'username': user.pk, 
            'password': user.email
            })