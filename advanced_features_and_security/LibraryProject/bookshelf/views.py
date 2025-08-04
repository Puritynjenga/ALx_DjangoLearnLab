from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
"""View to list all books."""
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context = {
        'list_books': books,
    }
    return render(request, 'bookshelf/list_books.html', context)

