from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=25)
    #email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title    