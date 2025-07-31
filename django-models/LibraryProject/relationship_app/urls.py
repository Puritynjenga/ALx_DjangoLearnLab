from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView
from django.urls import include
from . import views
urlpatterns = [
    
    path('books/', views.list_books, name='books-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.registerView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),
    path('add_book/', views.can_add_book, name='can_add_book'),
    path('edit_book/', views.can_change_book, name='can_change_book'),    
    path('delete_book/', views.can_delete_book, name='can_delete_book'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('register/', views.register_view, name='register'),


]
