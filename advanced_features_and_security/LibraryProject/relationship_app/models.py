import django
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

class Author(models.Model):
    """Model representing an author."""         
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
   
class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    class Meta:
        # Custom permissions for the Book model
    
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),]

    
    def __str__(self):
        return self.title   
    
class Library(models.Model):
    """Model representing a library."""
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    """Model representing a librarian."""
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')
    
    def __str__(self):
        return self.name        
     
class UserProfile(models.Model):
    """Model representing a user profile."""
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50, choices=[('Librarian', 'Librarian'), ('Member', 'Member'),('Admin','Admin')], default='member')   

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    


