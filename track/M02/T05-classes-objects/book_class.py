class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

title = input().strip()
author = input().strip()
price = int(input())

book = Book(title,author,price)

print("BOOK DETAILS")
print("Title:", book.title)
print("Author:", book.author)
print("Price: ", book.price)
