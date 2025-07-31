import django
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth import login
from django.contrib import messages

class CustomUserManager(BaseUserManager):
    """Custom user manager for the User model."""
    
    def create_user(self, email, username,password=None, **extra_fields):
        """Create and return a user with an email and password."""
        if not email:
            raise ValueError('The email field must be filled out')
        if not username:
            raise ValueError('The username field must be filled out')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username,email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        return self.create_user(username, email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    """Custom user model."""
    email = models.EmailField(unique=True, max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True, null=True)

    objects = CustomUserManager()


    USERNAME_FIELD = 'useraname'
    REQUIRED_FIELDS = ['email']
     

    def __str__(self):
        return f"{self.username} - {self.email}"
    
    
class Author(models.Model):
    """Model representing an author."""         
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
   
class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField(null=False)
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
    


