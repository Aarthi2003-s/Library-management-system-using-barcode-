# books/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def edit_book(request, access_no):
    book = get_object_or_404(Book, access_no=access_no)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

def delete_book(request, access_no):
    book = get_object_or_404(Book, access_no=access_no)
    if request.method == 'POST':
        book.borrow_set.all().delete()  
       
        book.delete()
        return redirect('book_list')
    
    return render(request, 'books/delete_book.html', {'book': book})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
