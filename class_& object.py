class Author:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def write_book(self,book_title):
        book=Book(book_title)
        self.books.append(book)
        book.author=self
class Book:
    def __init__(self,title):
        self.title=title
        self.author=None

# Create the instance of the author and the book
author_1=Author("James clear and stefen hawking")
book_1=Book("Atomic habits and Brief history of time")

#Establishing the link between objects

author_1.write_book(book_1.title)

#Accessing the objects through the link
print(author_1.books[0].title)
# print(book_1.author.name)