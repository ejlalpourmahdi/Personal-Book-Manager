import json

class Bookshelf():
    def __init__(self, books):
        self.books = books

    def showBooks(self):
        print("\n================ Your books ================\n")

        for book in self.books:
            print(f"- Name: {book["name"].title()}\n- Author: {book["author"].title()}\n- Category: {book["category"]}")
            print("\n---\n")

    def saveBooks(self):
        with open("books.json", "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=2)

    def loadBooks(self):
        try:
            with open("books.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []