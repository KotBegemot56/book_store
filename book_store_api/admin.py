from django.contrib import admin

from book_store_api.models import Book, Author

admin.site.register(Author)
admin.site.register(Book)