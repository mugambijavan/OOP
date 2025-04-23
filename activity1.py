class Book:
    def __init__(self, title, author, publication_year, genre):
        """
        Initializes a Book object with its title, author, publication year, and genre.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.is_borrowed = False

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"Title: {self.title}, Author: {self.author} ({self.publication_year}), Genre: {self.genre}"

    def borrow(self):
        """
        Marks the book as borrowed if it's not already.
        """
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        """
        Marks the book as returned.
        """
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

# Inheritance Layer: EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, publication_year, genre, file_format):
        """
        Initializes an EBook object, inheriting from Book and adding file format.
        """
        super().__init__(title, author, publication_year, genre)
        self.file_format = file_format
        self.is_downloaded = False

    def __str__(self):
        """
        Extends the string representation to include the file format.
        """
        return f"{super().__str__()} [EBook - Format: {self.file_format}]"

    def download(self):
        """
        Marks the ebook as downloaded.
        """
        if not self.is_downloaded:
            self.is_downloaded = True
            print(f"'{self.title}' has been downloaded in '{self.file_format}' format.")
        else:
            print(f"'{self.title}' is already downloaded.")

# Creating Book and EBook objects
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "Science Fiction")
ebook1 = EBook("Pride and Prejudice", "Jane Austen", 1813, "Romance", "EPUB")

print(book1)
print(ebook1)

book1.borrow()
ebook1.download()
book1.return_book()
ebook1.borrow() # EBook inherits the borrow method