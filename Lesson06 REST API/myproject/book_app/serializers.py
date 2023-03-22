from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True, source="book_set")
    class Meta:
        model = Author
        fields = ['id', 'name', 'email','books']