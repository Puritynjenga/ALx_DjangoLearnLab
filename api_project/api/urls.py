from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet 
from django.urls import include 
# Create a router and register our viewset with it
router = DefaultRouter()
# Register the viewset with a basename
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    #Route for the BooList view(ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    # Include the router's URLs for BookViewSet(all CRUD operations)
    path('', include(router.urls)),

]