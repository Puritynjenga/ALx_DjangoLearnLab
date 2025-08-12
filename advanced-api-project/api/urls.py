from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
# This file defines the URL patterns for the API, mapping each endpoint to its corresponding view.
# The URL patterns include paths for listing, retrieving, creating, updating, and deleting books.
# Each path is associated with a view class that handles the request and response logic for that endpoint.
# The `name` parameter allows for easy reference to these URL patterns in templates or when using Django's reverse URL resolution.
# The `pk` in the paths for detail, update, and delete views refers to the primary key of the book instance being accessed, allowing for specific book operations.  
# The `BookListView` handles GET requests to list all books, while `BookDetailView` retrieves a specific book by its primary key.
# The `BookCreateView` allows authenticated users to create new book entries, while `BookUpdateView` and `BookDeleteView` allow for updating and deleting existing books, respectively.