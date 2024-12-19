from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer

class AuthorListCreate(generics.ListCreateAPIView): # GET POST
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView): # GET PUT PATCH - Частично обновить данные автора. DELETE
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
