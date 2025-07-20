from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic import DetailView,ListView

# Create your views here.
def list_book(request):
    books = Book.objects.all()
    context= {
        'books_list': books,  
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['books'] = self.object.books.all()
    #     return context
    def get_books_in_library(self):
        #prefetch related books to avoid N+1 query problem
        return Library.objects.prefetch_related('books')
    