class Book:  # class
    print("Book class is being created")
    a = 5 # property

    def abc(self): # method
        print("This is a method of Book class")

book1 = Book()  # object
print(book1.abc()) # calling method