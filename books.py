class Bookshelf():
    def __init__(self, books):
        self.books = books

    def showBooks(self):

        print("\n================ Your books ================\n")

        for book in self.books:
            print(f"- Name: {book["name"].title()}\n- Author: {book["author"].title()}\n- Category: {book["category"]}")
            print("\n---\n")