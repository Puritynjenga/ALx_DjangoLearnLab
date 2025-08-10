from django.shortcuts import render
from .models import Book, Author
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView, RedirectView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  
from django.contrib import messages 
from django.contrib.auth import login
from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
# Create your views here.
class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']




class UserListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'publication_year']
def ListView(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'api/book_list.html', {'books': books})
  
def DetailView(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'api/book_detail.html', {'books': books})
    
@permission_required('api.add_book')   
@login_required    
def CreateView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        
        author = Author.objects.get(id=author_id)
        book = Book.objects.create(title=title, author=author, publication_year=publication_year)
        
        return render(request, 'api/book_detail.html', {'book': book})
@permission_required('api.delete_book')
@login_required
def DeleteView(request):
    if request.method == 'POST':
        book_id = request.POST.get('id')
        book = Book.objects.get(id=book_id)
        book.delete()
        return render(request, 'api/book_list.html', {'message': 'Book deleted successfully.'})
     
       
@permission_required('api.update_book')    
@login_required
def UpdateView(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)
        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        
        return render(request, 'api/book_detail.html', {'book': book})
    
    else:
        book = Book.objects.get(id=id)
        return render(request, 'api/book_update.html', {'book': book})