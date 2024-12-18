from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'publisher', 'category')
    search_fields = ('title', 'author__first_name', 'author__last_name')
