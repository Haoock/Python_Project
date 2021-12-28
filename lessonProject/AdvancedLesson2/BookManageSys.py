class BookManager:
    def __init__(self):
        # state为0表示没有被借出
        book1 = {"Name": "Python", "Author": "Guido", "Position": "INS888", "State": 0}
        book2 = {"Name": "Java", "Author": "Hello", "Position": "IGS888", "State": 0}
        book3 = {"Name": "C", "Author": "Westos", "Position": "INS880", "State": 0}
        self.bookList = [book1, book2, book3]

    def find_book(self, book_name):
        book_flag = False
        for book in self.bookList:
            if book["Name"] == book_name:
                print("Name: %s" % book['Name'])
                print("Author: %s" % book["Author"])
                print("State: %d" % book['State'])
                print("Position: %s" % book['Position'])
                book_flag = True
                break
        if not book_flag:
            print("Book is not exist")

    def add_book(self, name, author, position):
        book = {"Name": name, "Author": author, "Position": position, "State": 0}
        self.bookList.append(book)
        print("Add book successfully！")

    def borrow_book(self, book_name):
        book_flag = False
        for book in self.bookList:
            if book["Name"] == book_name:
                book_flag = True
                if book['State'] == 0:
                    print("Book %s was borrowed successfully!" % book["Name"])
                    book['State'] = 1
                else:
                    print("Failed,Book %s is already borrowed !" % book["Name"])
                break
        if not book_flag:
            print("Book %s is not exits!" % book_name)

    def return_book(self, book_name):
        book_flag = False
        for book in self.bookList:
            if book["Name"] == book_name:
                book_flag = True
                if book['State'] == 1:
                    book['State'] = 0  # 还书
                    print("Return Book %s successfully!" % book["Name"])
                else:
                    print("Failed,This book is already in bookshelf.")
                break
        if not book_flag:
            print("Book %s is not exits!" % book_name)


bookManager = BookManager()
while True:
    print("1.查询\n2.增加\n3.借阅\n4.归还\n5.退出")
    choice = int(input(""))
    if choice == 1:
        book_name = input("Book name:")
        bookManager.find_book(book_name)
    elif choice == 2:
        book_name = input("Book name:")
        book_author = input("Book author:")
        book_position = input("Book Position:")
        bookManager.add_book(book_name, book_author, book_position)
    elif choice == 3:
        book_name = input("Please enter your book name:")
        bookManager.borrow_book(book_name)
    elif choice == 4:
        book_name = input("Please enter your book name:")
        bookManager.return_book(book_name)
    elif choice == 5:
        print("Are you sure you want to exit the system?(Y/N)")
        answer = input("")
        if answer == "Y":
            print("Thank you for using!")
            break
        elif answer == 'N':
            pass




