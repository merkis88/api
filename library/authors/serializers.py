from rest_framework import serializers
from .models import Author
from books.models import Book

class AuthorSerializer(serializers.ModelSerializer):
    # Поле для ввода списка книг в одной строке
    books = serializers.CharField(write_only=True)  # Пользователь вводит названия через запятую

    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        # Извлекаем строку с названиями книг
        book_titles = validated_data.pop('books', '')

        # Разбиваем строку на список названий книг
        book_titles = [title.strip() for title in book_titles.split(',') if title.strip()]

        # Создаём автора
        author = Author.objects.create(**validated_data)

        # Создаём или связываем книги
        for title in book_titles:
            book, created = Book.objects.get_or_create(title=title)
            book.author = author
            book.save()

        return author
