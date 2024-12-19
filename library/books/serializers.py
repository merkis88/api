from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    # Заменяем `author` на обычное текстовое поле
    author = serializers.CharField()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        # Получаем значение автора из данных
        author_name = validated_data.pop('author')

        # Разделяем имя и фамилию (если нужно)
        first_name, last_name = author_name.split()

        # Пытаемся найти автора или создаём его
        author, created = Author.objects.get_or_create(
            first_name=first_name,
            last_name=last_name
        )

        # Привязываем автора к книге
        validated_data['author'] = author

        # Создаём и возвращаем книгу
        return super().create(validated_data)
