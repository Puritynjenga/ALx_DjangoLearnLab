from .models import Author,Book,Librarian,Library
from django.db import models

#query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        Author.objects.filter(author=author).select_related('books')
        return author.books.all()
    except Author.DoesNotExist:
        return None
    
#list all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        Library.objects.filter(library=library).select_related('books')
        # Retrieve all books in the library
        return library.books.all()
    except Library.DoesNotExist:
        return None
    #Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.filter(library=library).first()
    except Library.DoesNotExist:
        return None