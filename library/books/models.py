from django.db import models
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    year = models.IntegerField(null=True, blank=True, default=None)
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    file = models.FileField(upload_to='books/', blank=True, null=True)

    class Meta:
        unique_together = ('title', 'author', 'year', 'publisher')

    def __str__(self):
        return self.title
