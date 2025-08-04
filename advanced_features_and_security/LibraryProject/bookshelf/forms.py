from django import forms
from .models import Book
from django.core.exceptions import ValidationError
from datetime import datetime 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'publication_year': forms.NumberInput(attrs={'placeholder': 'Enter publication year'}),
        }
    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year:
            current_year = datetime.now().year
            if year > current_year:
                raise ValidationError('Enter a valid year. Publication year cannot be in the future.')
        return year
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Title cannot be empty.')
        return title
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise ValidationError('Author cannot be empty.')
        return author
    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
        return book    

      