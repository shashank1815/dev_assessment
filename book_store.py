class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
    def get_age(self):
        return 2026 - self.publication_year
    def get_summary(self):
        return(
            f"Title:{self.title},"
            f"Author:{self.author},"
            f"Published: {self.publication_year}"
        )
#create 3 Book objects

book1 = Book("Hary Potter and the Philosopher's Stone",
             "J.K. Rowling",
             "978-0-7475-3269-9",
             1997,
)
book2 = Book("The Alchemist",
             "Paulo Coelho",
             "0-06-250217-4",
             1988,
)
book3 = Book("A Man Called Ove",
             "Fredrik Backman",
             "9781476738024",
             2012,
)

# Print details
books = [book1, book2, book3]
for book in books:
    print("Title:", book.title)
    print("Author:", book.author)
    print("ISBN:", book.isbn)
    print("Age:", book.get_age())
    print("Summary:", book.get_summary())
    print()