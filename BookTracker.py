class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1  # Start reading on page 1!

    def info(self):
        print(f"‘{self.title}’ by {self.author} – {self.pages} pages total.")

    def read(self, pages_read):
        self.current_page += pages_read
        # Make sure we don't go past the last page
        if self.current_page > self.pages:
            self.current_page = self.pages
            print("You read the entire book! 🎉 Try a new one now.")
        print(f"You read {pages_read} pages. You are now on page {self.current_page}.")

    def bookmark(self):
        print(f"You are on page {self.current_page} of '{self.title}'.")


# Test it!
my_book = Book("Diary of A Wimpy Kid", "Jeff Kinney", 247)
my_book.info()
my_book.bookmark()
my_book.read(50)    
my_book.bookmark()
my_book.read(200)   
my_book.bookmark()
my_book.read(100)   
my_book.bookmark()