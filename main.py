
__starter__ = """
|``````````````````````````````|
| WELCOME TO THE PEACELIBRARY. |
|______________________________|
"""
__action__ = """
1. Display Book
2. Lend Book
3. Add Book
4. Return Book
"""

class Library:

    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lend_book_list = []

    def display_book(self):
        print(f"Availabe books in our '{self.name}'")
        print("------------------------------------")
        for book in self.booklist:
            print(f"{book}")
        print("------------------------------------\n")

    def lend_book(self, book):
        if book in self.booklist:
            if book in [item['book'] for item in self.lend_book_list]:
                print(f"This Book is already being used.")
                print(f"You can pick another book you wan't.\n")
            else:
                user = input("Enter Your Name : ")
                print(f"{book} is avalable. You can take the book now.\n")
                self.lend_book_list.append({"book": book, "user": user})
        else:
            print(f"|X| Book is not available in our Library, Please Try Another Book! |X|\n")

    def add_Book(self, user):
        if user == "AnuragNagar":
            book = input("Enter the Book you want to Add : \n")
            self.booklist.append(book)
            print(f"Book has been added to the Booklist : {book}")
        else:
            print("|X| You are not 'Authorized' to add the Book. |X|\n")

    def return_book(self, book):
        if book in self.booklist:
            value = [item for item in self.lend_book_list if item['book'] != book]
            print(value)
            self.lend_book_list = value
            print("Thank you for returning our Book, Please visit again.")
        else:
            print(f"'{book}' is not in record of our 'Library' booklists.")


if __name__ == '__main__':
    library = Library(["Rich Dad Poor Dad",
                            "7 Habits of Highly Effective People",
                            "The Courage to Create",
                            "The Power Of Now",
                            "The Power Of Positive Thinking",
                            "The Defining Decades",
                            "Complete Work of Swami Vivekananda",
                            "The Power Of Subconcious Mind",
                            "7 Law Of Human Nature"], "PeaceLibrary")

    print(__starter__)
    while True:
        print("Enter your choice to Continue:")
        print(__action__)

        user_choise = input("Enter : ")

        print(f"Your choice is : {user_choise}\n")

        if user_choise == "1":
            library.display_book()

        elif user_choise == "2":
            library.display_book()
            book = input("Enter the Book you want to lend : ")
            library.lend_book(book)

        elif user_choise == "3":
            user = input("Please Enter Username : ")
            library.add_Book(user)

        elif user_choise == "4":
            book = input("Enter the name of the book you want to return : ")
            library.return_book(book)

        else:
            print("|X| Please enter a valid option. |X|\n")
            continue

        while True:
            print("Press 'q' to quit and 'c' to continue")
            user_choise2 = input("->")
            if user_choise2 == "q":
                print("Thank's for visit!")
                exit()
            elif user_choise2 == "c":
                break
            else:
                print("|X| Please enter a valid option. |X|\n")
                continue
