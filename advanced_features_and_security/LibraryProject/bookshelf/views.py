from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ExampleForm
# Create your views here.
"""View to list all books."""
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):

    search_query = request.GET.get('search', '').strip()
    
    books = Book.objects.all()
    if search_query:
        search_query = re.sub(r'\s+', ' ', search_query)  # Normalize whitespace
        search_query = search_query.lower()
        books = books.filter(title__icontains=search_query)
   
    # Sort books based on the query parameter
    sort_by = request.GET.get('sort', 'title').lower()
    match sort_by:
        case 'year':
            books = books.order_by('publication_year')
        case 'title':
            books = books.order_by('title')
        case 'author':
            books = books.order_by('author')
        case _:
            books = books.order_by('title', 'author', 'publication_year')
    # Ensure books are unique
    books = books.distinct()     
            
    # Paginate to limit the number of books displayed per page
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page', 1)
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    
    context = {
        'list_books': books,
    }
    return render(request, 'bookshelf/list_books.html', context)

