from django.shortcuts import render,redirect
from .models import Book
from .forms import CreateBookForm, UpdateBookForm

# Create your views here.

def view_book(request):
    all_books = Book.objects.all()
    if request.method == 'POST':
        create_book = CreateBookForm(request.POST)
        if create_book.is_valid():
            create_book.save()
            return redirect('books:view_book')
    else:
        create_book = CreateBookForm()

    context = {
        'all_books': all_books,
        'create_form':create_book
    }
    return render(request,'book/display_books.html',context)

def delete_book(request,book_id):
    get_book = Book.objects.get(id=book_id)
    get_book.delete()
    return redirect('books:view_book')

def update_book(request,update_id):
    get_book = Book.objects.get(id=update_id)
    if request.method == 'POST':
        update_form = UpdateBookForm(request.POST,instance=get_book)
        if update_form.is_valid():
            update_form.save()
            return redirect('books:view_book')
    else:
        update_form = UpdateBookForm(instance=get_book)


    context = {
        'update_book':update_form
    }
    return render(request,'book/update_books.html',context)