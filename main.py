username = input("Please enter your name: ")

print(f"Welcome {username}!")



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
        print("Success!")
        break