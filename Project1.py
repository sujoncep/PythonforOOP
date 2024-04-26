# # class Libaray:
# #     def __init__(self, list, name):
# #         self.booklist = list
# #         self.name = name
# #         self.lenDict = {}

# #     def displayBooks(self):
# #         print(f"{self.name}, We have following books in our library")
# #         sno = 1
# #         for book in self.booklist:
# #             print(f"{sno} {book}")
# #             sno = sno+1

# #     def lendBook(self, book, name):
# #         if book in self.booklist:
# #             if book not in self.lenDict:
# #                 self.lenDict.update({book: name})
# #                 print(
# #                     "Leadner book database has been updated. You can take the book now.")

# #             else:
# #                 print(f"Book is already being used by {self.lenDict[book]} ")

# #     def addBook(self, book):
# #         self.booklist.append(book)
# #         print(f" Your book {book} has been added in to the book list.")

# #     def returnBook(self, book):
# #         if book in self.booklist:
# #             if book in self.lenDict.keys():
# #                 self.lenDict.pop(book)
# #             else:
# #                 print(f"This book is {book} not in use.")
# #         else:
# #             print("This book is not relate to our database.")


# # BenLibrary = Libaray(['python', 'java', 'data science',
# #                      'web scraping', 'data mining'], 'Ben')

# # print(BenLibrary.__dict__)
# # # print(BenLibrary.displayBooks())
# # # BenLibrary.addBook('django')
# # # BenLibrary.lendBook('data science', 'John')


class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lenDict = {}

    def displayBooks(self):
        print(f"{self.name}, We have these follwong books in our library.")
        sno = 1
        for book in self.bookList:
            print(f"{sno} {book}")
            sno += 1

    def lendBook(self, book, name):
        if book in self.bookList:
            if book not in self.lenDict:
                self.lenDict.update({book: name})
                print(
                    "Lender-Book databse has been updated. Your can take the book now.")
            else:
                print(
                    f"Book is already being used by \"{self.lenDict[book]}\"")
        else:
            print(f"This book is not relate to our database.")

    def addBook(self, book):
        self.bookList.append(book)
        print(f"Your book \"{book}\" has been added to the book list.")

    def returnBook(self, book):
        if book in self.bookList:
            if book in self.lenDict.keys():
                self.lenDict.pop(book)
                print(f"Thank you ,Your book \"{book}\" is recived.")
            else:
                print(f"This book \"{book}\" is not in use.")

        else:
            print(f"This book \"{book}\" is not relate to our database.")


# Execusion code
if __name__ == '__main__':

    BenLibrary = Library(['Python', 'Java', 'Data Science',
                         'Web Scraping', 'Data Mining'], 'Ben')
    while (True):
        print(
            f"Welcome to the \"{BenLibrary.name}\" library. \n Please Enter your choice to continue")
        print("1 Display Books")
        print("2 Lend a Book")
        print("3 Add a Book")
        print("4 Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid choice number")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            BenLibrary.displayBooks()

        elif user_choice == 2:
            book = input("Entet the name of the book you want to lend:")
            user_name = input("Your name please:")
            BenLibrary.lendBook(book, user_name)

        elif user_choice == 3:
            book = input("Entet the name of the book you want to add:")
            BenLibrary.addBook(book)

        elif user_choice == 4:
            book = input("Entet the name of the book you want to return:")
            BenLibrary.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")

        user_choice2 = ""

        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
