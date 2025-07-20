from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView,ListView
from django.urls import reverse_lazy
from django_backups import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout,signup
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context= {
        'list_books': books,  
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
    
class registerView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'registration/register.html'

class LoginView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/login.html'

class LogoutView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('logout')
    template_name = 'registration/logout.html'   


    