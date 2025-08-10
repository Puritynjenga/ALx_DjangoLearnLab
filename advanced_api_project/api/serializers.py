from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

'''Serializers define the API representation of the models.
They convert model instances into JSON format and validate incoming data. 
the bookSerializer is used to serialize and deserialize Book model instances.
the validation logic ensures that the publication year is not set in the future and raises a validation error'''
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year', 'isbn']

        def validate_publication_year(self, value):
            if value > datetime.date.today():
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value

'''the nested bookSerializer is used to include related book data in the Author serializer.
This allows you to retrieve an author's information along with the books they have written.'''    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
