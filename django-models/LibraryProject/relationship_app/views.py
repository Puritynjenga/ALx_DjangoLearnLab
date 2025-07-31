from django.shortcuts import render,redirect
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django .contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    """Updated registration view using custom user form."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('list_books')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})


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

    def get_books_in_library(self):
        #prefetch related books to avoid N+1 query problem
        return Library.objects.prefetch_related('books')
    
class registerView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Register')
    template_name = 'relationship_app/register.html'

class LoginView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Login')
    template_name = 'relationship_app/login.html'

class LogoutView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Logout')
    template_name = 'relationship_app/logout.html'   
    
def  is_admin(user):
    """Check if the user is an admin."""
    return user.is_authenticated and user.profile.role == 'admin'  
def is_librarian(user):
    """Check if the user is a librarian."""
    return user.is_authenticated and user.profile.role == 'librarian'
def is_member(user):
    """Check if the user is a member."""
    return user.is_authenticated and user.profile.role == 'member'

@login_required
@user_passes_test(is_admin,login_url='/Login/')
def admin_view(request):
    """View for admin users."""
    return render(request, 'relationship_app/admin_view.html') 

      
@login_required
@user_passes_test(is_librarian,login_url='/Login/')
def librarian_view(request):
    """View for librarian users."""
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member,login_url='/Login/')
def member_view(request):
    """View for member users."""
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def can_add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author =request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        Book.objects.create(title=title, author=author, publication_date=publication_date)
        messages.success(request, 'Book added successfully.')
        return redirect('list_books')
@permission_required('relationship_app.can_change_book') 
def can_change_book(request,book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_date = request.POST.get('publication_date')
        book.save()
        messages.success(request, 'Book updated successfully.')
        return redirect('list_books')

@permission_required('relationship_app.can_delete_book')
def can_delete_book(request,book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        book.delete()
        messages.success(request, 'Book deleted successfully.')
        return redirect('list_books')
    else:
        messages.error(request, 'You do not have permission to delete this book.')
        return redirect('list_books')