from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
  

    def __str__(self):
        return self.title
    
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