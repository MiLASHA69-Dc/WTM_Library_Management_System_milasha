from django.contrib import admin
from .models import Book,BookRequest
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.


class BookAdmin(ImportExportActionModelAdmin):
    list_display = [
        "title","isbn","author","published_date"
    ]

admin.site.register(Book, BookAdmin)    

@admin.register(BookRequest)
class BookRequestAdmin(ImportExportActionModelAdmin):
    list_display = [
        "id","customer","book","date_of_request","date_of_return"
    ]

   