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
]