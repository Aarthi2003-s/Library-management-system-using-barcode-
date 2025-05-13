# views.py
from django.shortcuts import render
from books.models import Book
from borrow.models import Borrow

def search_books(request):
    query = request.GET.get("q", "").strip()
    results = []
    message = ""

    if query:
        results = Book.objects.filter(title__icontains=query) | \
                  Book.objects.filter(author__icontains=query) | \
                  Book.objects.filter(isbn__icontains=query)

        if not results:
            message = "No books found matching your search."

    books_data = []
    for book in results:
        is_borrowed = Borrow.objects.filter(book=book, is_returned=False).exists()
        status = "Unavailable (Borrowed)" if is_borrowed else "Available"
        books_data.append({
            "access_no": book.access_no,  # Include access_no
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "status": status
        })

    return render(request, "booksearch/search_books.html", {"books": books_data, "query": query, "message": message})
