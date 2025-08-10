from django.urls import path
from .views import ListView, DetailView, CreateView, DeleteView 
from django.conf.urls import include    
from django.contrib import admin

# URL patterns for the API
# These patterns map to the views defined in api/views.py
# Each view corresponds to a specific action on the Book model
# such as listing books, viewing details, creating a new book, or deleting a book.  

urlpatterns = [
    path('books/', ListView, name='book-list'),
    path('books/<int:id>/', DetailView, name='book-detail'),
    path('books/create/', CreateView, name='book-create'),
    path('books/delete/', DeleteView, name='book-delete'),
]
