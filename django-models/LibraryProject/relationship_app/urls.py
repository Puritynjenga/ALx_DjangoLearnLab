from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.books_list, name='books_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail')
]
