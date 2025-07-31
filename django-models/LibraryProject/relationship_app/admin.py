from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Library, Author, Librarian, UserProfile


class CustomModelAdmin(UserAdmin):
    """Custom admin configuration for the User model."""
    model = User
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

admin.site.register(User, CustomModelAdmin)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(UserProfile)


