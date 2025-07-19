#CRUD operations on python shell

#create a book instance 
from bookshelf.models import Book
book = Book.objects.create(
	title = "1984",
	author = "George Orwell",
	publication_year = "1949")
#retrieve all the books
book.Book.objects.all()
book.Book.get(id=1)

#update the author
book.title = "Nineteen Eighty-Four"
book.save()

#delete book
book.delete()

