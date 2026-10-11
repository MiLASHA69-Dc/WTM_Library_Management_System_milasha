from django.urls import path
from .views import view_book, delete_book, update_book


app_name = 'books'
urlpatterns = [
    path('view-books/',view_book,name='view_book'),
    path('delete-books/<str:book_id>/', delete_book, name='delete_book'),
    path('update-books/<str:update_id>',update_book,name='update_books'),
    
]