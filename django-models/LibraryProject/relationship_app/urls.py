from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView
from django.urls import include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='books-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
]