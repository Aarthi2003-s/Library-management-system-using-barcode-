from django.contrib import admin
from books.models import Book  # Import Book from the books app

class BookSearchAdmin(admin.ModelAdmin):
    list_display = ("isbn", "title", "author")
    search_fields = ("isbn", "title", "author")

admin.site.register(Book, BookSearchAdmin)
