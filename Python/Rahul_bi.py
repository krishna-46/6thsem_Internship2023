# Create a library instance
library = Library()

# Add books to the library
library.add_book("Book 1", "Author 1", 100)
library.add_book("Book 2", "Author 2", 200)
library.add_book("Book 3", "Author 1", 150)
library.add_book("Book 4", "Author 3", 400)
library.add_book("Book 5", "Author 2", 250)

# Use map to create a new list of book titles
book_titles = list(map(lambda book: book.title, library.books))
print(book_titles)  # Output: ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5']

# Use filter to create a new list of books with more than 300 pages
books_over_300_pages = list(filter(lambda book: book.num_pages > 300, library.books))
print([book.title for book in books_over_300_pages])  # Output: ['Book 4']

# Use reduce to calculate the total number of pages in the library
from functools import reduce
total_pages = reduce(lambda acc, book: acc + book.num_pages, library.books, 0)
print(total_pages)  # Output: 1100

# Use the get_books_by_author method to get a list of books by a specific author
books_by_author = library.get_books_by_author("Author 1")
print([book.title for book in books_by_author])  # Output: ['Book 1', 'Book 3']