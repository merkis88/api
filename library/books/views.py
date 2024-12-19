from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Поиск
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__first_name', 'author__last_name']