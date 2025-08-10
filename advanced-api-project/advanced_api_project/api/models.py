from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
    publication_year = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    