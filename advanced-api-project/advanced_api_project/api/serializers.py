from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

'''Serializers define the API representation.
This serializer will be used to convert the Book model instances into JSON format
and validate incoming data for creating or updating Book instances.'''
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['__all__']  # Include all fields from the Book model
        

# this method validates the publication year to ensure it is not in the future

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value       

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']        