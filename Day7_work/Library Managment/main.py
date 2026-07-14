from book import Book
from member import Member

book1 = Book("Python Basics","Alice","ISBN001")
book2 =Book("Learning OOP","Bob","ISBN002")
book3 =Book("Data Science 101","Charlie","ISBN003")

for b in [book1, book2, book3]:
    b.display()

member1 = Member("Alice",101)
member2 = Member("Bob",102)

member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book3)
member2.borrow_book(book1)

member1.display_books()
member2.display_books()

member1.return_block(book2)
member2.borrow_book(book2)