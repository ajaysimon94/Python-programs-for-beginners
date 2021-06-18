from datetime import datetime

while True:

    class library():

        def __init__(self,bl,library_name):
            self.book_list = bl
            self.lname = library_name

        def display_book():
            print("The list of available books are:")
            print(*library.book_list, sep = "\n")
            library.loop_func()

        def lend_book():
            # for item in username_list:
            #     if username == item:
            #         print("Please select any other username")
            #         library.lend_book()
            #     else:
            #         print("Thank you for entering your username")
            print("Which book would you like to borrow\n")
            lend_book = input()
            today = str(datetime.today())
            for item in library.book_list:
                if lend_book == item: #if the book is available
                    print("The book you requested is avaiable")
                    lend_book2 = lend_book+" : "+"[lent to library on "+today+"]"
                    library.book_list.remove(lend_book)
                    print(f"Thank you {username}, the book - {lend_book} has been assigned to you")
                    lend_dict[username] = lend_book2
                    lend_dict1[username] = lend_book
                    library.loop_func()
                else:
                    for key, value in lend_dict1.items():
                        if lend_book == value:
                            print(f"Sorry, this book is unavailable now. It's borrowed by {key}")
                            library.loop_func()
                    else:
                        print("This book is not available with us yet.")
                        print("Would you like to borrow another book? - Y or N")
                        borrow_another = input()
                        if borrow_another == "Y" or borrow_another == "y":
                            library.lend_book()
                        elif borrow_another == "N" or borrow_another == "n":
                            print("OK. Taking you back to main screen")
                            library.loop_func()
                        else:
                            print("incorrect input")

        def add_book():
            print("Which books would you like to add to your library")
            print("Note: If you are entering multiple books, please seperate the names using a comma only")
            add_book1 = input()
            seperate = add_book1.split(",")
            for items in seperate:
                library.book_list.append(items)
            library.loop_func()

        def return_book():
            print("Enter the name of the book you are returning")
            rtr_book = input()
            library.book_list.append(rtr_book)
            print("Getting here")
            for key,value in lend_dict1.items():
                if rtr_book == value:
                    print(lend_dict1[value])
            # del lend_dict[rtr_book]
            else:
                print("Else statement")
            library.loop_func()

        def change_user():
            global username
            print("You are currently logged in as" + username)
            print("Enter new login ID")
            username = input()
            username_list.append(username)
            print(f"You have now logged in as {username}")
            library.main_menu()

        def view_login():
            print(username_list)
            library.main_menu()

        def lend_account():
            print(lend_dict1)
            library.main_menu()

        def main_menu():
            print("What would you like to do:\n Press 1 to display books\n Press 2 to lend book\n "
                  "Press 3 to add new books \n Press 4 to return a book\n Press 5 to login as another user\n "
                  "Press 6 to view all login IDs in the system\n Press 7 to view lend book account" )
            a = int(input())
            if a == int(1):
                library.display_book()
            elif a == int(2):
                library.lend_book()
            elif a == int(3):
                library.add_book()
            elif a == int(4):
                library.return_book()
            elif a == int(5):
                library.change_user()
            elif a == int(6):
                library.view_login()
            elif a == int(7):
                library.lend_account()
            else:
                print("You have entered incorrect input. Please enter your input again")
                library.main_menu()

        def loop_func():
            # print("Would you like to continue? Y or N")
            # cont = input()
            # if cont == "Y" or cont == "y":
                library.main_menu()
            # else:
            #     print(f"Thank you for using {library.lname} library management system")
            #     quit()



    print("What would you like to name your library?\n")
    library.lname=input()
    print("Please mention the list of books to be added in your library\n")
    input_string = input()
    library.book_list = input_string.split(",")

    print(f"Welcome to {library.lname} library management system\n")

    lend_dict = {}
    lend_dict1 = {}
    username_list = []
    print("Please enter your username\n")
    username = input()
    username_list.append(username)

    library.main_menu()


