from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Genre

# Register your models here.

#@admin.register(Genre)

class GenreAdmin(ImportExportModelAdmin):
    list_display = [
        "id","title","category"
    ]

admin.site.register(Genre,GenreAdmin)