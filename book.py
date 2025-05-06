class Book:
    # Class variable to track the total number of books
    total_books = 0
    
    def __init__(self, title, author):
        """
        Constructor to initialize a new Book object with a title and an author.
        Each time a new book is created, the total book count is incremented.
        """
        self.title = title
        self.author = author
        # Increment the book count whenever a new book is created
        Book.total_books += 1
    
    def display_info(self):
        """
        Displays the title and author of the book.
        """
        print(f"Title: {self.title}, Author: {self.author}")
    
    @classmethod
    def display_total_books(cls):
        """
        Class method to display the total number of books in the library.
        """
        print(f"Total books in library: {cls.total_books}")
    
    @classmethod
    def increment_book_count(cls):
        """
        Class method to manually increment the book count.
        """
        cls.total_books += 1
        print(f"Book count incremented. New count: {cls.total_books}")
    
    @classmethod
    def reset_book_count(cls):
        """
        Class method to reset the total book count to zero.
        """
        cls.total_books = 0
        print("Book count has been reset to 0")

# Example usage
if __name__ == "__main__":
    # Display the initial count of books (should be 0)
    Book.display_total_books()  # Total books in library: 0
    
    # Create some books, which will automatically increment the book count
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    
    # Display the updated book count after creating books
    Book.display_total_books()  # Total books in library: 2
    
    # Manually increment the book count (for testing)
    Book.increment_book_count()  # Book count incremented. New count: 3
    
    # Create another book, automatically increasing the count
    book3 = Book("1984", "George Orwell")
    
    # Display the final book count
    Book.display_total_books()  # Total books in library: 4
    
    # Reset the book count to zero
    Book.reset_book_count()  # Book count has been reset to 0
    Book.display_total_books()  # Total books in library: 0
