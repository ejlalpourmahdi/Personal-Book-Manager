from books import Bookshelf

username = input("Please enter your name: ")

print(f"Welcome {username}!")

books = []
bookshelf = Bookshelf(books)
savedBooks = bookshelf.loadBooks()
for sb in savedBooks:
    books.append(sb)

while True:
    print("\n================ New Book ================\n")

    bookName = input("Name: ")
    bookAuthor = input("Author: ")
    bookCategory = input("Category: ")

    print("\n==========================================\n")

    if bookName.strip() == "":
        print("Error! Book name can't be empty.\n")
    elif bookAuthor.strip() == "":
        print("Error! Please enter the author's name.\n")
    elif bookCategory.strip() == "":
        print("Error! Book Category can't be empty.\n")
    else:

        book = {
            "name": bookName,
            "author": bookAuthor,
            "category": bookCategory
        }

        books.append(book)

        print("Success!\n")

    repeat = input("\nDo you want to add a new book? (y/n): ")

    if repeat.lower() == "n":
        break
    elif repeat.lower() == "y":
        continue


bookshelf.showBooks()
bookshelf.saveBooks()