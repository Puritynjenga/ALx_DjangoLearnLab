from django.contrib import admin
from .models import Book
from  django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Book# Register your models here.

class CustomUserAdmin():
    """Custom admin configuration for the User model."""
    model = CustomUser
    list_display = ['username', 'email','is_staff', 'is_superuser', 'is_active', 'date_of_birth', 'profile_photo']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
            ('Personal Information', {             
                'fields': ('date_of_birth',),
                'description': 'Additional personal details about the user.'
            }),
            ('Media Files', {                      
                'fields': ('profile_photo',),
                'description': 'Profile image and other media files.'
            }),
        )
        
    add_fieldsets = UserAdmin.add_fieldsets + (
            ('Personal Information', {
                'fields': ('email', 'date_of_birth', 'profile_photo'),
            }),
        )
        
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('published_date',)



admin.site.register(Book)
admin.site.register(CustomUser, CustomUserAdmin)
