class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("This book (" + self.title + ") is written by " , self.author)
Cool_Book= Book("Hilo", "Judd Winick")