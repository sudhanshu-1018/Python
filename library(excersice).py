class library:

    def __init__(self) -> None:
        self.no_of_books=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)

    def showinfo(self):
        print(f"the library has {self.no_of_books} books.The books are:")
        for book in self.books:
            print(book)

l1=library()
l1.addbook("harry potter")
l1.addbook("sochiye aur ameer baniye")
l1.addbook("bade soch ka bada jadu")
l1.addbook("rich dad poor dad")
l1.showinfo()





#library using dictionary
class library:
    def __init__(self) -> None:
        self.no_of_books=0
        self.books={}        #dictionary

    def print_books(self):
        print("books:")
        for book,category in self.books.items():           #for key,value in self.book.items()
            print("- ",book, "(category:", category,")")   #print(f"the category of the {book} is {category}")

    def add_book(self,book,category):
        self.books[book]=category    #dictionary[key]=value  (adding a value to a new key)
        self.no_of_books +=1

    def get_no_of_books(self):
        return self.no_of_books
    
#object
library=library()

#show the initial number of books
print("final number of books:",library.get_no_of_books())

#add books
while True:
    print("Enter a book name (Enter 'q' to quit and get the total info):")
    book=input()
    if book =='q':
        break
    print("Enter the category of the book:")
    category=input()
    library.add_book(book,category)   #missing 2 required positional arguments

#show the final number of books:
print("Final number of books:",library.get_no_of_books())


#print all books
library.print_books()