from django.shortcuts import render,redirect
from .models import Book,BookRequest
from .forms import CreateBookForm, UpdateBookForm, BookRequestForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def view_book(request):
    all_books = Book.objects.all().select_related("author").prefetch_related("genre")
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

@login_required
def delete_book(request,book_id):
    get_book = Book.objects.get(id=book_id)
    get_book.delete()
    return redirect('books:view_book')

@login_required
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

@login_required
def make_book_request(request):
    current_user = request.user  #current user who is logged into the system now
    get_book_request = BookRequest.objects.filter(customer=current_user).select_related("book")
    
    
    create_book_request_form = BookRequestForm()
    if request.method=="POST":
        create_book_request_form = BookRequestForm(request.POST)
        if create_book_request_form.is_valid():
            request_form = create_book_request_form.save(commit=False)
            request_form.customer=current_user
            book_status = request_form.book
            if book_status.status=="av":
                book_status.status="br"
                book_status.save(
                    update_fields=[
                        "status"
                        ])
            request_form.save()
            return redirect ("books:book_request") #app name from urls.py is books

    context = {
        "request_form":create_book_request_form,
        "request_table":get_book_request,
    } 

    return render(request,"book_request/bookrequest.html",context)           

