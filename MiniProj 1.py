# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


# book_lenders = {Book:Name}
# book_lenders = {Key:Value}


class Library:
    book_list = ["book1", "book2", "book3", "book4", "book5", "book6", "book7", "book8"]

    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.lend_record = {}

    def displaybooks(self):
        for i in range(len(self.book_list)):
            print(f"{i + 1} . {self.book_list[i]}")
        print(f"Books Currently lent")
        for k, v in self.lend_record.items():
            print(f"{k} is lent by {v}")

    def addbooks(self):
        book = input("Enter book name:")
        self.book_list.append(book)
        print(f"{book} added successfully")

    def lendbook(self):
        book = input("Enter book name:")
        name = input("Enter your name:")
        if book in self.book_list:
            self.book_list.remove(book)
            self.lend_record[book] = name
            print(f'lending...')
            print(f'lent successfully !!')
        elif book not in self.book_list and book in self.lend_record.keys():
            print(f'{book} is already lent by {self.lend_record[book]}')
        else:
            print(f'sorry {book} is not available')

    def retnbook(self):
        book = input("Enter book name:")
        if book in self.lend_record.keys():
            self.book_list.append(book)
            del self.lend_record[book]
        else:
            print(f'{book} enter valid entry')

robin = Library(book_list= Library.book_list , library_name = 'robin_library' )



print('Welcome to Library')

while True:

    option = input(
        'Press\n''1. For Display\n''2. For Adding a book\n' '3. For Lending a book\n' '4. For returning a book\n''5. For EXIT')

    if option == "1":
        robin.displaybooks()
    elif option == "2":
        robin.addbooks()
    elif option == "3":
        robin.lendbook()
    elif option == "4":
        robin.retnbook()
    elif option == "5":
        break
    else:
        print("Please enter valid input")

