from book_store_api.models import Author, Book, Sell
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = "__all__"
